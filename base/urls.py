from django.urls import path
from base import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path




urlpatterns = [
    path("", views.loginpage, name="loginpage"),
    path('home.html',views.homepage, name='homepage'),
    path('login.html',views.loginpage, name='loginpage'),
    path('shop.html',views.shoppage, name='shoppage'),
    path('logout_user',views.logout_user, name='logout'),
    path('signup.html',views.signuppage, name='signuppage'),
    path('sale.html',views.salepage, name='salepage'),
    
    

]
urlpatterns+=staticfiles_urlpatterns()