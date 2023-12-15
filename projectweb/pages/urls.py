from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import registration, profile

app_name = 'pages'


urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('rules/', TemplateView.as_view(template_name='pages/rules.html'),
         name='rules'),
    path('registr/', registration,
         name='registr'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('profile/', profile,
         name='profile'),
]
