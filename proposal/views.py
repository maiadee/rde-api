from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Proposal

from .serializers.common import ProposalSerializer
from .serializers.populated import PopulatedProposalSerializer

class UserProposalListView(APIView):
    # * need authentication here

    # index
    def get(self, request):
        submitted_proposals = Proposal.objects.all()
        serialized_proposals = PopulatedProposalSerializer(submitted_proposals, many=True)
        return Response(serialized_proposals.data)
    
    # create
    def post(self, request):
        new_proposal = ProposalSerializer(data=request.data)
        if new_proposal.is_valid():
            new_proposal.save()
            return Response(new_proposal.data, 201)

        return Response(new_proposal.errors, 422)


# Regular all proposal list view for admin
    # * Authentication
    #  filter per talent 