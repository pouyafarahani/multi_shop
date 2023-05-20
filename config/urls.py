from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
                  # Django admin
                  path('admin/', admin.site.urls),

                  # User management
                  path('accounts/', include('django.contrib.auth.urls')),

                  # local apps
                  path('', include('apps.home.urls')),
                  path('accounts/', include('apps.accounts.urls')),
                  path('products/', include('apps.products.urls')),
                  path('contact/', include('apps.contact.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
