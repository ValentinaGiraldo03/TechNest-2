from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
]