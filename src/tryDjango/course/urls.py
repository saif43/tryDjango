from django.urls import path
from .views import (
    my_fbv
)

app_name = 'course'


urlpatterns = [
    path("",my_fbv, name="course-list")    
]
