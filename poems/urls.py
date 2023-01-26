from django.urls import path
from .views import PoemListView, PoemDetailView, PoemTitleSearchView, PoemIndexSearchView

urlpatterns = [
    path('', PoemListView.as_view()),
    path('<int:pk>/', PoemDetailView.as_view()),
    path('search-titles/', PoemTitleSearchView.as_view()),
    path('poem-index/', PoemIndexSearchView.as_view())
]
