from django import forms

from ..models.contact_us import ContactModel


class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['subject', 'message']
