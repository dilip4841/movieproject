from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.index, name = 'home_page'),
    path('genres_movie/<slug:language>',views.dispaly_genre, name='genre'),
    path('movinfo/<slug:mid>',views.display_movieinfo, name="movieinfo"),
    path('sign_upform/',views.login_form, name='singupform'),
    path('login_form/',views.login, name='loginform'),
    path('logout_form/', views.logout, name='logoutform'),
]
