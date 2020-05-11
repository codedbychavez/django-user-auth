# user_auth > urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from user import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Accounts pattern
    path('accounts/', include('django.contrib.auth.urls')),
    # Sign-up pattern
    url(r'^signup/$', views.signup, name='signup'),
    # Home pattern
    path('home/', TemplateView.as_view(template_name='home.html')),
]
