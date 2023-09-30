from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catig/<int:catid>/', views.categ, name='categ')
]