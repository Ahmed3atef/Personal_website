from django.urls import path
from .views import SignUpView,ProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]
