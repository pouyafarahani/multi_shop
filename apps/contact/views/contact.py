from django.contrib import messages
from django.shortcuts import render
from django.views import View

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
            messages.success(request, 'Thank you for your comment')
        else:
            messages.warning(request, 'Enter the information correctly')

        return render(request, self.template_name, {'form': form})
