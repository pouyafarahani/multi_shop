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
                  path('', include('home.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('products/', include('products.urls')),
                  path('contact/', include('contact.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
