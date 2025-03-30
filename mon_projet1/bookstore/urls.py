from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home , name = 'home'),
    path('constomer/' , views.constomer , name = "constomer" ),
    path('product/' , views.product , name = "product"),
    path('base/' , views.base , name = "base"),

]
