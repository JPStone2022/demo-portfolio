"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
# admin is no longer used in the database-less version
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# static files are handled by WhiteNoise in production for a database-less setup
# from django.conf.urls.static import static

urlpatterns = [
    # The admin path is removed as django.contrib.admin is not used
    # path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), # Include URLs from the portfolio app
]

# The MEDIA_URL and MEDIA_ROOT are not configured for the database-less version,
# as user-uploaded media files typically require database interaction for model fields.
# Static files (CSS, JS, project images hardcoded in static_data.py) are handled
# by Django's staticfiles app in development and WhiteNoise in production.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This line is removed
