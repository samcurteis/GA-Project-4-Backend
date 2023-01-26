from django.urls import path
from .views import AuthorListView, AuthorPopularView, AuthorDetailView, AuthorSearchView, AuthorIndexView

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('popular/', AuthorPopularView.as_view()),
    path('<int:pk>/', AuthorDetailView.as_view()),
    path('search/', AuthorSearchView.as_view()),
    path('index/', AuthorIndexView.as_view())
]
