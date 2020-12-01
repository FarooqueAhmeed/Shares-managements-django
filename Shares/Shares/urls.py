from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path("add_shares", views.add_shares, name="add_shares"),
    #path('edit_share/<share_id>', views.edit_share, name='edit_share'),
    path('delete_share/<share_id>', views.delete_share, name='delete_share'),

   # path('delete/<task_id>', views.delete_task, name='delete_task'),
   # path('edit/<task_id>', views.edit_task, name='edit_task'),

]
