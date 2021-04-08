from django.urls import path
from notes.views import home, newnote


urlpatterns = [
    path('', home, name='home'),
    path('newnote/',newnote,name='newnote')
]