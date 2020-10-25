from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]