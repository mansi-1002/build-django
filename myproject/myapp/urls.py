from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_view, name='get_view'),
    path('post/', views.post_view, name='post_view'),
    path('put/', views.put_view, name='put_view'),
    path('delete/', views.delete_view, name='delete_view'),
]

