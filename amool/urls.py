from django.urls import path
from . import views




urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('admin_dashboard/', views.dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('cars/', views.cars_view, name='cars'),    
    path('reservation/', views.reservation, name='reservation'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('offers/', views.offers, name='offers'),
    path('add_car/', views.add_car, name='add_car'),
    path('list_car/', views.list_car, name='list_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
]
