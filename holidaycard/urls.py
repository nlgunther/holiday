from django.urls import path
from . import views

urlpatterns = [
    path('', views.card2018, name='card2018.html'),
    path(r'test',views.card2018wip, name='card2018wip.html'),
]

