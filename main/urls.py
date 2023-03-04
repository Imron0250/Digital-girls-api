from django.urls import path
from .views import *

urlpatterns = [
    path('get-info/', info_site),
    path('get-import-screen/', import_screen),
    path('get-about-project/', get_about_project),
    path('get-direction-about/', get_direction_about),
    path('get-direction-more/', get_direction_more),
    path('get-tasks/', get_tasks),
    path('get-result/', get_result),
    path('register/', register),
]
