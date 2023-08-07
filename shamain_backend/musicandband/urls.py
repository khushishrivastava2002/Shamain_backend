from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from.views import *

urlpatterns = [
    path('Musicandband/', Musicandband,name='Musicandband'),
    path('Musicandband/female', Mfemale,name='Mfemale'),
    path('Musicandband/male', Mmale,name='Mmale'),
    path('Musicandband/all', Musicandband,name='Musicandband'),
    #--------------------------------------------------------------------------
    path('Movieandseries/', Movieandseries1,name='Movieandseries1'),
    path('Movieandseries/female', Mofemale,name='Mofemale'),
    path('Movieandseries/male', Momale,name='Momale'),
    path('Movieandseries/all', Movieandseries1,name='Movieandseries'),
    #--------------------------------------------------------------------------
    path('Sports/', Sports1,name='Sports1'),
    path('Sports/female', Sfemale,name='Sfemale'),
    path('Sports/male', Smale,name='Smale'),
    path('Sports/all', Sports1,name='Sports1'),
    #--------------------------------------------------------------------------
    path('Persona/', Persona1,name='Persona1'),
    path('Persona/female', Pefemale,name='Sfemale'),
    path('Persona/male', Pemale,name='Smale'),
    path('Persona/all', Persona1,name='Persona1'),
    #--------------------------------------------------------------------------
    path('Dripdoodle/', Dripdoodle1,name='Dripdoodle1'),
    path('Dripdoodle/female', Dfemale,name='Sfemale'),
    path('Dripdoodle/male', Dmale,name='Smale'),
    path('Dripdoodle/all', Dripdoodle1,name='Dripdoodle1'),
    #--------------------------------------------------------------------------
    path('Anime/', Anime1,name='Anime1'),
    path('Anime/female', Abfemale,name='Abfemale'),
    path('Anime/male', Abmale,name='Abmale'),
    path('Anime/all', Anime1,name='Anime1'),
    #--------------------------------------------------------------------------
    path('Abstract/', Abstract1,name='Abstract1'),
    path('Abstract/female', Anfemale,name='Sfemale'),
    path('Abstract/male', Anmale,name='Smale'),
    path('Abstract/all', Abstract1,name='Abstract1'),
    #--------------------------------------------------------------------------
    path('Comics/', Comics1,name='Comics1'),
    path('Comics/female', Cfemale,name='Cfemale'),
    path('Comics/male', Cmale,name='Cmale'),
    path('Comics/all', Comics1,name='Comics1'),
    #--------------------------------------------------------------------------
    path('Sanskriti/', Sanskriti1,name='Sanskriti1'),
    path('Sanskriti/female', Safemale,name='Safemale'),
    path('Sanskriti/male', Samale,name='Samale'),
    path('Sanskriti/all', Sanskriti1,name='Sanskriti1'),
    #--------------------------------------------------------------------------
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)