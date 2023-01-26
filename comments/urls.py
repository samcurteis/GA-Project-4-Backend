from django.urls import path
from .views import CommentListView, CommentDetailView, CommentSearchView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('search/', CommentSearchView.as_view())
]
