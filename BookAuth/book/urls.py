from django.urls import path
from django.urls import path
from .views import BookListView, BookCreateView
from .views import BookUpdateDeleteView
from .views import RegisterView, LoginView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('books_list/', BookListView.as_view()),
    path('books_create/', BookCreateView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('books/<int:pk>/', BookUpdateDeleteView.as_view()),
]

