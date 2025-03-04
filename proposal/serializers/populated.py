from .common import ProposalSerializer
from talent.serializers.common import TalentNameSerializer
from users.serializers.common import UserSerializer

class PopulatedProposalSerializer(ProposalSerializer):
    talent = TalentNameSerializer()
    user = UserSerializer()

