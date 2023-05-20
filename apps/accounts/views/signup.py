from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms.signup import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"