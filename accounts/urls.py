from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="home"),
    path('Login', views.Login, name="Login"),
    path('register', views.Register, name="register"),
    path('Profile', views.Profile, name="profile"),
    path('logout', views.logout, name="logout"),
    path('uploadPost', views.uploadPost, name="uploadPost"),
    path('posts', views.Posts, name="posts"),
    path('search', views.searchFriends, name="serachFriends"),
    path('addFollowers', views.addFollowers, name="addFollowers"),
    path('Feeds', views.Feeds, name="Feeds")

]
