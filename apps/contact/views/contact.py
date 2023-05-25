from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from ..forms.form_contact import ContactForms


class ContactView(View):
    template_name = 'contact/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForms(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
        return render(request, self.template_name, {'form': form})
