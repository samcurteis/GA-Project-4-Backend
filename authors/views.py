from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError

from django.db.models import Q
from .serializers.common import AuthorSerializer
from .serializers.populated import PopulatedAuthorSerializer
from .models import Author


class AuthorListView(APIView):
    def get(self, _request):
        authors = Author.objects.all()
        serialized_authors = AuthorSerializer(authors, many=True)
        return Response(serialized_authors.data, status=status.HTTP_200_OK)

    def post(self, request):
        author_to_add = AuthorSerializer(data=request.data)
        try:
            author_to_add.is_valid()
            author_to_add.save()
            return Response(author_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class AuthorPopularView(APIView):
    def get(self, _request):
        authors = Author.objects.order_by('favorites')[:6]
        serialized_authors = AuthorSerializer(authors, many=True)
        return Response(serialized_authors.data, status=status.HTTP_200_OK)


class AuthorDetailView(APIView):
    def get(self, _request, pk):
        author = Author.objects.get(pk=pk)
        serialized_author = PopulatedAuthorSerializer(author)
        return Response(serialized_author.data, status=status.HTTP_200_OK)

    def delete(self, _request, pk):
        try:
            author_to_delete = Author.objects.get(pk=pk)
            author_to_delete.delete()
            return Response({"detail": "Author successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            raise NotFound(detail="Author not found")

    def put(self, request, pk):
        author_to_edit = Author.objects.get(pk=pk)
        updated_author = AuthorSerializer(author_to_edit, data=request.data)

        try:
            updated_author.is_valid()
            updated_author.save()
            return Response(updated_author.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class AuthorSearchView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        results = Author.objects.filter(name__icontains=query)
        serialized_results = AuthorSerializer(results, many=True)
        return Response(serialized_results.data)


class AuthorIndexView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        results = Author.objects.filter(Q(name__istartswith=query) | Q(
            name__istartswith=f"the {query}"))
        serialized_results = AuthorSerializer(results, many=True)
        return Response(serialized_results.data)
