from .common import AuthorSerializer
# absolute paths in django have the manage.py file as the root
from poems.serializers.common import PoemSerializer

#  Genre serializer gets us the standard fields (in this case it's going to return {"id":1, "name": "blues"})


class PopulatedAuthorSerializer(AuthorSerializer):
    poems = PoemSerializer(many=True)
