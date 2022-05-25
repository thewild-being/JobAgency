"""
hyperjob URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

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
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('menu.urls')),
    path('vacancies', include('vacancy.urls')),
    path('resumes', include('resume.urls')),
    path('home', include('home.urls')),

    path('login', include('user_login.urls_login')),
    path('logout', include('user_logout.urls_logout')),
    path('signup', include('user_signup.urls')),
    # to avoid messing w redirection in the relative views: RedirectView.as_view() 
    # we need redirection to avoid setting APPEND_SLASH = False when using POST/GET methods
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),

]
