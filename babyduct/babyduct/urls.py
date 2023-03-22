"""babyduct URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from accounts.api.views import FacebookLogin, TwitterLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/v1/auth/facebook", FacebookLogin.as_view(), name="facebook_login"),
    # path('api/v1/auth/google', GoogleLogin.as_view(), name='google_login'),
    # path("api/v1/auth/twitter", TwitterLogin.as_view(), name="twitter_login"),
    path('api/v1/accounts/', include('accounts.api.urls')),
    
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'accounts-schema'}
    ), name='swagger-ui'),

    path('accounts-api-schema', get_schema_view(
        title="BabyDuct User Accounts and Authentication Schema",
        description="API for BabyDuct Users",
        version="1.0.0"
    ), name='accounts-schema'),
]

urlpatterns += staticfiles_urlpatterns()
