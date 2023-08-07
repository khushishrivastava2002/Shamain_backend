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
    
    path('Movieandseries/', Movieandseries1,name='Movieandseries1'),
    path('Movieandseries/female', Mofemale,name='Mofemale'),
    path('Movieandseries/male', Momale,name='Momale'),
    path('Movieandseries/all', Movieandseries1,name='Movieandseries'),
    
    path('Sports/', Sports1,name='Sports1'),
    path('Persona/', Persona1,name='Persona1'),
    path('Dripdoodle/', Dripdoodle1,name='Dripdoodle1'),
    path('Anime/', Anime1,name='Anime1'),
    path('Abstract/', Abstract1,name='Abstract1'),
    path('Comics/', Comics1,name='Comics1'),
    path('Sanskriti/', Sanskriti1,name='Sanskriti1'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)