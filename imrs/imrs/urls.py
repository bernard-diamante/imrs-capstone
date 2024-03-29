"""imrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import RedirectView
from dashboard.views import LandingPageView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('item/', include('item.urls')),
    path('project_site/', include('project_site.urls')),
    path('requisition/', include('requisition.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('transfer/', include('transfer.urls')),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("select2/", include("django_select2.urls")),
    path('contact-admin/', TemplateView.as_view(template_name="contact-admin.html"), name='contact_admin')
]
