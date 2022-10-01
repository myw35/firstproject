
from django.urls import path
from django.contrib.auth import views as auth_views
from common import views 

app_name = 'common'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('browse/', views.browse, name='browse'),
    path('Movie1/', views.Movie1, name='Movie1'),
    path('Movie2/', views.Movie2, name='Movie2'),
    path('Movie3/', views.Movie3, name='Movie3'),
    path('Movie4/', views.Movie4, name='Movie4'),
]



