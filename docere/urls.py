
"""docere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import index
from .settings import MEDIA_ROOT, MEDIA_URL
from apps.registration.views import profile
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)


urlpatterns = [
    path('', index, name="home"),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include("apps.registration.urls")),
    path('information/', include("apps.information.urls")),
    path('virtualroom/', include("apps.virtualroom.urls")),
    path('evaluation/', include("apps.evaluation.urls")),
    path("accounts/profile/", profile, name="myprofile"),

    # api urls
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include("docere.api.routes")),

]


