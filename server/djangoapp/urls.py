from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Added a trailing slash to 'login/' (Django best practice)
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Route for registration functionality
    path('register', views.registration, name='register'),
]

# Safely serve media/static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)