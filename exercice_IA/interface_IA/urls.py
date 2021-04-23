from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('list/', views.ImagesListView.as_view(), name='image_list'),
    path('delete/<pk>', views.ImagesDelete.as_view(), name='image_delete'),
    path('delete/', views.ImagesDelete.as_view(), name='image_delete'),
]
