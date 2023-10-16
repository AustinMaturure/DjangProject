# Import necessary modules
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

# Definning URL patterns using urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL pattern
    # Include practice app's URLs under /articles/
    re_path(r'^articles/', include('practice.urls')),
    # Include accounts app's URLs under /accounts/
    re_path(r'accounts/', include('accounts.urls')),
    # Include practice app's URLs for the root path
    path('', include('practice.urls')),
]

# static URL patterns for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
