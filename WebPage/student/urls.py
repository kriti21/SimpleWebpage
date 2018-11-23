from django.urls import path

from . import views

urlpatterns = [
	path('', views.enterstudent, name='enterstudent'),
	path('enterstudent/', views.enterstudent, name='enterstudent'),
    path('liststudents/', views.liststudents, name='liststudents'),
]