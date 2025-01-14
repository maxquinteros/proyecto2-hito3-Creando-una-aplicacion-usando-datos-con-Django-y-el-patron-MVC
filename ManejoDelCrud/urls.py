from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from web.views import index, usuario, login, register, editar_perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('usuario/', editar_perfil, name='usuario'),
]
