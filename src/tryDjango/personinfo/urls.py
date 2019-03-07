from django.contrib import admin
from django.urls import path
from .views import person_create_view, person_list_view, dynamic_lookup_view

app_name = 'personinfo'

urlpatterns = [
    path('create', person_create_view, name='person-create'),
    path('view', person_list_view, name='person-showall'),
    path('<int:id>', dynamic_lookup_view, name='person-detail'),
]
