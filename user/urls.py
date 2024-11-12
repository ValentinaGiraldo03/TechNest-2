from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/client/', views.register_client, name='register_client'),
    path('register/administrator/', views.register_administrator, name='register_administrator'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('addProduct/', views.add_product, name='add_product'),
    path('editProduct/<int:producto_id>/', views.edit_product, name='edit_product'),
    path('deleteProduct/<int:producto_id>/', views.delete_product, name='delete_product'),
]
