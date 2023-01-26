from django.urls import path
from .views import PostListView, PostDetailView, PostSearchView, RecentPostListView

urlpatterns = [
    path('', PostListView.as_view()),
    path('recent/', RecentPostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('search/', PostSearchView.as_view())
]
