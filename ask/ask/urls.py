"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf   # WARNING:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import adminfi
from django.urls import path, re_path
from qa.views import test, index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', test, name='test'),
    path('signup/', test, name='test'),
    re_path(r'question/(?P<id>\d+)/', test, name='test'),
    path('ask/', test, name='test'),
    path('popular/', test, name='test'),
    path('new/', test, name='test'),
]
