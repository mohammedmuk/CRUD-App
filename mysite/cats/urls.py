from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('lookup/', views.BreadList.as_view(), name='bread_list'),
    path('lookup/create/', views.BreadCreate.as_view(), name='bread_create'),
    path('lookup/<int:pk>/update/', views.BreadUpdate.as_view(), name='bread_update'),
    path('lookup/<int:pk>/delete/', views.BreadDelete.as_view(), name='bread_delete'),
]