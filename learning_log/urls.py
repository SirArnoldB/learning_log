"""learning_log URL Configuration

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

# the first two lines import a module and a function to manage URSLs for the admin site
# the body of the file defines the urlpatterns variable

urlpatterns = [
    path('admin/', admin.site.urls),
    # this will match any url that starts with the word users. 
    path('users/', include('users.urls')), 
    # include the module learning_logs.urls
    path('', include('learning_logs.urls')), 
]
