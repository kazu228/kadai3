from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('', views.top, name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('form/', views.form, name='form'),
    path('confirm/', views.confirm, name='confirm'),
    path('signup/', views.signup, name='signup'),
]
