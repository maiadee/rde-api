from .common import TalentSerializer
from proposal.serializers.common import ProposalSerializer

class PopulatedTalentSerializer(TalentSerializer):
    recieved_proposal = ProposalSerializer(many=True)