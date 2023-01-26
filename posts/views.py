from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.db import IntegrityError

from .models import Post
from .serializers.common import PostSerializer
from .serializers.populated import PopulatedPostSerializer


class RecentPostListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        posts = Post.objects.order_by('-created_at')[:6]
        serialized_posts = PopulatedPostSerializer(posts, many=True)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)


class PostListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        posts = Post.objects.order_by('post_favorites')[:6]
        serialized_posts = PopulatedPostSerializer(posts, many=True)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['author'] = request.user.id
        post_to_add = PostSerializer(data=request.data)
        try:
            post_to_add.is_valid()
            post_to_add.save()
            return Response(post_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PostDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound(detail="Can't find that post!")

    def get(self, _request, pk):
        post = self.get_post(pk=pk)
        serialized_post = PopulatedPostSerializer(post)
        return Response(serialized_post.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post_to_edit = self.get_post(pk=pk)
        updated_post = PostSerializer(post_to_edit, data=request.data)
        try:
            updated_post.is_valid()
            updated_post.save()
            return Response(updated_post.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        post_to_delete = self.get_post(pk=pk)
        post_to_delete.delete()
        return Response({"detail": "Post successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class PostSearchView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        results = Post.objects.filter(title__icontains=query)
        serialized_results = PopulatedPostSerializer(results, many=True)
        return Response(serialized_results.data)
