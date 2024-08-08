"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from socialsite import views
from config.django import base
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('base',views.base,name='base'),
    path('logout',views.logout,name='logout'),
    path('create-post',views.create_post,name='create_post'),
    path('post_list',views.post_list,name='post_list'),
    path('update-post/<int:pk>/', views.update_post, name='update_post'),
    path('del-post/<int:pk>/', views.del_post, name='del_post'),
    path('main/',views.main,name='main'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.post_like, name='post_like'),
    path('post/<int:post_id>/comment/', views.comment, name='comment'),
]
urlpatterns += static(base.STATIC_URL,document_root=base.STATIC_ROOT)
urlpatterns += static(base.MEDIA_URL,document_root=base.MEDIA_ROOT)