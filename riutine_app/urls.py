from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name = 'about'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('check_in/<list_id>', views.check_in, name='checkin'),
    path('check_out/<list_id>', views.check_out, name= 'checkout'),
    path('edit/<list_id>', views.edit, name='edit')

]