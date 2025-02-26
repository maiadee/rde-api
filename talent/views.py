from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .serializers.common import TalentSerializer
from .models import Talent

# Create your views here.

class TalentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        talent_queryset = Talent.objects.all()
        talent_serialized = TalentSerializer(talent_queryset, many=True)
        return Response(talent_serialized.data)
   
    def post(self, request):
        talent_serializer = TalentSerializer(data=request.data)
        if talent_serializer.is_valid():
            talent_serializer.save()
            return Response(talent_serializer.data, 201)
        else:
            return Response(talent_serializer.errors, 422)
        

class TalentDetailView(APIView):
    

    def get_talent(self, talent_id):
        try:
            talent = Talent.objects.get(id=talent_id)
            return talent
        except Talent.DoesNotExist as e:
            raise NotFound('Talent not found')

    def get(self, request, talent_id):
        talent = self.get_talent(talent_id)
        serialized_talent = TalentSerializer(talent)
        return Response(serialized_talent.data)
 
    
    def put(self, request, talent_id):
        talent = self.get_talent(talent_id)  
        serialized_talent = TalentSerializer(talent, data=request.data)  
    
        if serialized_talent.is_valid():
            serialized_talent.save()
            return Response(serialized_talent.data)
    
        return Response(serialized_talent.errors, 422)

        
    def delete(self, request, talent_id):
        talent = self.get_talent(talent_id)
        talent.delete()
        return Response({"message": "Talent deleted successfully"}, status=204)