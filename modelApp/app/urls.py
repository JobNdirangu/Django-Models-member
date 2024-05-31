from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addmember', views.add, name='addmember'),
    path('registermember', views.register_member, name='registermember'),
    path('delete_member/<int:id>', views.delete_member, name='delete_member'),
    path('get_member/<int:id>', views.get_member, name='get_member'),
    path('update_member/<int:id>', views.update_member, name='update_member')
]