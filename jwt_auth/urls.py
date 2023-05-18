from django.urls import path
from .views import RegisterView
from .views import LoginView, UserListView, UserDetailView, UserSearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('search/', UserSearchView.as_view())
]
