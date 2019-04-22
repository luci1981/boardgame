from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home, name='home'),
    path('formular/', views.formular, name='formular'),
    path('formular_submit/', views.formular_submit, name='formular_submit'),
    path('person/', views.person, name='person'),
    path('persons/', views.persons, name='persons'),
    # path('deleteperson/<int:id>/', views.deleteperson, name='deleteperson'),
    re_path(r'deleteperson/<int:id>/$', views.deleteperson, name='deleteperson'),
]