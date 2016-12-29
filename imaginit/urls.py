"""imaginit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import urls
#add this import
#from django.contrib.auth import views
#from main.forms import LoginForm
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls, namespace="main", app_name="main")),
   url(r'^accounts/', include('allauth.urls')),
  #  url(r'^accounts/login/$', views.login),
  #  url(r'^accounts/auth/$', views.auth_view),
  #  url(r'^accounts/logout/$', views.logout),
  #  url(r'^accounts/loggedin/$', views.loggedin),
  #  url(r'^accounts/login/$', views.invalid_login),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
