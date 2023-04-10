from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:pk>', views.customer_records, name='records'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('add-record/', views.add_records, name='add-records'),
    path('update-record/<int:pk>', views.update_records, name='update-records')


]