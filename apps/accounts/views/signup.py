from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView

from ..forms.signup import CustomUserCreationForm


@method_decorator(cache_page(600), name='dispatch')  # 600sec == 10 min
class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
