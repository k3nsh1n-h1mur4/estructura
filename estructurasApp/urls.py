from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('info/<str:field1>/', views.info, name='info'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('delete/<str:field1>/', views.delete, name='delete'),
    path('edit/<str:field1>/', views.edit,  name='edit'),
]
