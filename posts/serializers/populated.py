from .common import PostSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedPostSerializer(PostSerializer):
    author = UserSerializer()
    comments = PopulatedCommentSerializer(many=True)
