from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import IntegrityError
from django.db.models import Q

from .serializers.common import CommentSerializer
from .serializers.populated import PopulatedCommentSerializer
from .models import Comment


class CommentListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        comments = Comment.objects.all()
        serialized_comments = CommentSerializer(comments, many=True)
        return Response(serialized_comments.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        comment_to_add = CommentSerializer(data=request.data)
        try:
            comment_to_add.is_valid()
            comment_to_add.save()
            return Response(comment_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CommentDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, _request, pk):
        comment = Comment.objects.get(pk=pk)
        serialized_comment = PopulatedCommentSerializer(comment)
        return Response(serialized_comment.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            comment_to_delete = Comment.objects.get(pk=pk)
            if comment_to_delete.owner != request.user:
                raise PermissionDenied()
            comment_to_delete.delete()
            return Response({"detail": "Comment successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail="Comment not found")

    def put(self, request, pk):
        comment_to_edit = Comment.objects.get(pk=pk)
        if comment_to_edit.owner != request.user:
            raise PermissionDenied()
        updated_comment = CommentSerializer(comment_to_edit, data=request.data)

        try:
            updated_comment.is_valid()
            updated_comment.save()
            return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CommentSearchView(APIView):
    def get(self, request):
        query = request.GET.get('search')
        print(query)
        results = Comment.objects.filter(Q(content__icontains=query) | Q(
            created_at__icontains=query))
        serialized_results = CommentSerializer(results, many=True)
        return Response(serialized_results.data)
