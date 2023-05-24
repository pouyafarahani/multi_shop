from django.contrib import admin
from django.contrib.admin import register

from .models.contact_us import ContactModel


@register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    pass
