"""
URL configuration for Shopokoa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from myapp.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserListView)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('get_collection', views.get_collection, name='get_collection'),
    path('', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/add/', UserCreateView.as_view(), name='user_add'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('api/user/list/', views.user_list, name='user_list'),
    path('api/user/signup/', views.signup, name='signup'),
    path('api/user/signin/', views.signin, name='signin'),
    path('', include(router.urls)),
]
