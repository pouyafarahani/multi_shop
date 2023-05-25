from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms.signup import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "User account created successfully.")
        return response
