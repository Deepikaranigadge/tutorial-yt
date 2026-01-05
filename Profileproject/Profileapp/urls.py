from django.urls import path
from .views import student_profile

urlpatterns = [
    path('', student_profile, name='student_profile'),
]
