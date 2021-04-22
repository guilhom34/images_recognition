from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ImagesListView.as_view(), name='image_list'),
    path('delete/', views.ImagesDelete.as_view(), name='image_delete'),
    path('form_test', views.form_test, name='form_test'),
]