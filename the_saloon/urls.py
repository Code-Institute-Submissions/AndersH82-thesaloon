from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('shout_like/<int:pk>', views.shout_like, name="shout_like"),
    path('delete_shout/<int:pk>', views.delete_shout, name="delete_shout"),
    
]
