from .common import TalentSerializer
from proposal.serializers.common import ProposalSerializer

class PopulatedTalentSerializer(TalentSerializer):
    proposal = ProposalSerializer(many=True)