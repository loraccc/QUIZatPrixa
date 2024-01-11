from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('quiz/', quiz_category_selection, name='quiz_category_selection'),
    path('quiz/<int:category_id>/', quiz_view, name='quiz_view'),
    path('submit_quiz/<int:category_id>/', submit_quiz, name='submit_quiz'),
    path('quiz_result/', quiz_result, name='quiz_result'),
]