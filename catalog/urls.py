from django.urls import path
from .views import show_courses, create_course, update_course, confirm_delete_course, actually_delete_course  # .views refer to the views.py in the current directory as this file

urlpatterns = [
    path('', show_courses, name='show_courses'),
    path('create', create_course),
    path('update/<course_id>', update_course, name='update_course'),
    path('confirm_delete/<course_id>', confirm_delete_course),
    path('actually_delete/<course_id>', actually_delete_course, name='delete_course')
]