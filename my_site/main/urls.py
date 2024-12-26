from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ),
    path('tables', views.tables),
    path('regi', views.regi),
    path('auto', views.regi)
]