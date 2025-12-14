from django.urls import path
from . import views

urlpatterns = [
    path('', views.regvendor, name='regvendor'),
    path('reguser/', views.reguser, name='reguser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homepage/', views.homepage, name='homepage'),
    path('hoteldetail/<int:id>/', views.hoteldetail, name='hoteldetail'),
    path('add_menu/<int:id>/', views.add_menu, name='add_menu'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('franchise_details/<int:id>/', views.franchise_details, name='franchise_details'),
    path('emicalculation/<int:id>/', views.emicalculation, name='emicalculation'),
]
