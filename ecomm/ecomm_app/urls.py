
from django.urls import path
from ecomm_app import views

urlpatterns = [
   path('home',views.home),
   path('create',views.create),
   path('dashboard',views.dashboard),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.edit),

]
