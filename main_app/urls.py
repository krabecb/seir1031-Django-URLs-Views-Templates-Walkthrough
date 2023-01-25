from django.urls import path
from . import views

urlpatterns = [
    # '' => localhost:8000
    # views.Home => views.py => class Home
    # name: Helpful for navigation, we can simply say the success url (redirect) is the path named "home"
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('songs/', views.SongList.as_view(), name="song_list"),
]