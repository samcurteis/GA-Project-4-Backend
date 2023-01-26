from authors.serializers.common import AuthorSerializer, ReducedAuthorSerializer
from .common import PoemSerializer, ReducedPoemSerializer


class PopulatedPoemSerializer(PoemSerializer):
    author = AuthorSerializer()


class ReducedPopulatedPoemSerializer(ReducedPoemSerializer):
    author = ReducedAuthorSerializer()
