from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #AmiAmi Home Page
    path('about/', views.about, name='about'), #About Page
    path('login/', views.login_user, name='login'), #Login Page
    path('logout/', views.logout_user, name='logout'), #Logs out and return to home
    path('register/', views.register_user, name='register'), #registration page
    path('product/<int:pk>', views.product, name='product'), # Product page/ assigns unique id
    path('category/<str:foo>', views.category, name='category'), #Category page
]