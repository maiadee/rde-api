from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Proposal

from .serializers.common import ProposalSerializer
from .serializers.populated import PopulatedProposalSerializer

class UserProposalListView(APIView):
    permission_classes = [IsAuthenticated]

    # Get all proposals for logged-in user
    def get(self, request):
   
        submitted_proposals = Proposal.objects.filter(user=request.user)
        serialized_proposals = PopulatedProposalSerializer(submitted_proposals, many=True)
        return Response(serialized_proposals.data)
    
    # create
    def post(self, request):

        request.data['user'] = request.user.id
        new_proposal = ProposalSerializer(data=request.data)
        if new_proposal.is_valid():
            new_proposal.save(user=request.user)
            return Response(new_proposal.data, 201)

        return Response(new_proposal.errors, 422)
    


# Regular all proposal list view for admin
class AdminProposalListView(APIView):
    # * Authentication
    permission_classes = [IsAdminUser]

    def get(self, request):
        proposals = Proposal.objects.all()
        serializes_proposals = PopulatedProposalSerializer(proposals, many=True)
        return Response(serializes_proposals.data)

   
class SingleProposalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, proposal_id):
        try:
            proposal = Proposal.objects.get(id=proposal_id)
            serialized_proposal = PopulatedProposalSerializer(proposal)
            return Response(serialized_proposal.data)
        except Proposal.DoesNotExist as e:
            raise NotFound('Proposal not found')
        
    def put(self, request, proposal_id):
        try:
            # query
            proposal = Proposal.objects.get(id=proposal_id)
            # serialize
            serialized_proposal = ProposalSerializer(proposal, data=request.data, partial=True)
            # validate
            if serialized_proposal.is_valid():
                serialized_proposal.save()
                return Response(serialized_proposal.data)
            return Response(serialized_proposal.errors, 422)
        
        except Proposal.DoesNotExist as e:
            raise NotFound('Proposal not found')
        

    def delete(self, request, proposal_id):
        try:
            proposal = Proposal.objects.get(id=proposal_id)
            if request.user.is_staff or proposal.user == request.user:
                proposal.delete()
                return Response(status=204)
            else:
                return Response({"error": "You do not have permission to delete this proposal"}, status=403)
        except Proposal.DoesNotExist as e:
            raise NotFound('Proposal not found')