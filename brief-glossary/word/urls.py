from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.IndexView.as_view(), name='add'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
