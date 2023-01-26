from .common import UserSerializer

from poems.serializers.common import PoemSerializer
from poems.serializers.populated import PopulatedPoemSerializer
from posts.serializers.common import PostSerializer
from posts.serializers.populated import PopulatedPostSerializer
from comments.serializers.common import CommentSerializer
from authors.serializers.common import AuthorSerializer


class PopulatedUserSerializer(UserSerializer):
    poem_favorites = PopulatedPoemSerializer(many=True)
    poem_likes = PoemSerializer(many=True)
    post_favorites = PopulatedPostSerializer(many=True)
    post_likes = PostSerializer(many=True)
    favorite_authors = AuthorSerializer(many=True)
    posts = PostSerializer(many=True)
    comments = CommentSerializer(many=True)
