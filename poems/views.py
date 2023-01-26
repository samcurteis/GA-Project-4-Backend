from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from django.db.models import Q
from django.db import IntegrityError

from .models import Poem
from .serializers.common import PoemSerializer
from .serializers.populated import PopulatedPoemSerializer
from .serializers.common import ReducedPoemSerializer
from .serializers.populated import ReducedPopulatedPoemSerializer


class PoemListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        # get all albums from the database
        poems = Poem.objects.order_by('poem_favorites')[:6]
        serialized_poems = PopulatedPoemSerializer(poems, many=True)
        return Response(serialized_poems.data, status=status.HTTP_200_OK)

    def post(self, request):
        poem_to_add = PoemSerializer(data=request.data)
        try:
            poem_to_add.is_valid()
            poem_to_add.save()
            return Response(poem_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PoemDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_poem(self, pk):
        try:
            return Poem.objects.get(pk=pk)
        except Poem.DoesNotExist:
            raise NotFound(detail="Can't find that poem!")

    def get(self, _request, pk):

        poem = self.get_poem(pk=pk)
        serialized_poem = PopulatedPoemSerializer(poem)
        return Response(serialized_poem.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        poem_to_edit = self.get_poem(pk=pk)
        updated_poem = PoemSerializer(poem_to_edit, data=request.data)
        try:
            updated_poem.is_valid()
            updated_poem.save()
            return Response(updated_poem.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        poem_to_delete = self.get_poem(pk=pk)
        poem_to_delete.delete()
        return Response({"detail": "Poem successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class PoemTitleSearchView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        results = Poem.objects.filter(title__icontains=query)
        serialized_results = PopulatedPoemSerializer(results, many=True)
        return Response(serialized_results.data)


class PoemIndexSearchView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        results = Poem.objects.filter(Q(title__istartswith=query) | Q(
            title__istartswith=f"the {query}"))
        serialized_results = ReducedPopulatedPoemSerializer(results, many=True)
        return Response(serialized_results.data)
