from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('Musicandband/', Musicandband,name='Musicandband'),
    path('Movieandseries/', Movieandseries1,name='Movieandseries1'),
    path('Sports/', Sports1,name='Sports1'),
    path('Persona/', Persona1,name='Persona1'),
    path('Dripdoodle/', Dripdoodle1,name='Dripdoodle1'),
    path('Anime/', Anime1,name='Anime1'),
    path('Abstract/', Abstract1,name='Abstract1'),
    path('Comics/', Comics1,name='Comics1'),
    path('Sanskriti/', Sanskriti1,name='Sanskriti1'),
]