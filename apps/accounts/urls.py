from django.urls import path
from apps.accounts.views.signup import SignupPageView

urlpatterns = [
    path('register/', SignupPageView.as_view(), name='signup'),
]
