from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list , name='list'),
    path('add/',views.add , name='add'),
    path('update/<str:matricule>',views.update , name='update'),
    path('delete/<str:matricule>',views.delete , name='delete'),
    
]
