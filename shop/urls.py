from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name='main-page'),
    path('about/', views.about, name='about-page'),
    path('login/', views.login_user, name='login-page'),
    path('logout/', views.logout_user, name='logout-page'),
    path('signup/', views.signup_user, name='signup-page'),
    path('product/<int:id>/', views.product, name='product'),
    path('category/<str:name>/', views.category, name='category-page')
    ]
