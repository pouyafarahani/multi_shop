from django.shortcuts import render
from django.views import View

from ..forms.form_contact import ContactForms


class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')

    def post(self, request):
        form = ContactForms(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
        else:
            pass
        return render(request, 'contact/contact.html')
