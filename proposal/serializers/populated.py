from .common import ProposalSerializer
from talent.serializers.common import TalentNameSerializer

class PopulatedProposalSerializer(ProposalSerializer):
    talent = TalentNameSerializer()

