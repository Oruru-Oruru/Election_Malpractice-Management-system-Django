"""election_mailtpractice URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path,include

from election import views 

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('thanks/', views.thank, name='thanks'),
    path('evidence/', views.evidence, name='evidence'),
    path('category/',views.category,name='category'),
    path('category/<slug:slug>',views.category_detail,name='category_detail'),
    
    path('location/', views.location,name='location'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    
    
    path('logout/', views.logout_user, name='logout'),
    path('pdf/', views.pdf, name="pdf")
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
