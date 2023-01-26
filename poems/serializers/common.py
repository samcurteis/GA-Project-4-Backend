from rest_framework import serializers
from ..models import Poem


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'


class ReducedPoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('title', 'author', 'id')
