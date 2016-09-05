from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.MainView.as_view(), name="main_page"),
    url(r'^about_me/', views.about_me, name="about_me"),
    url(r'^toolbox/', views.toolbox, name="toolbox"),
    url(r'^news/', views.news, name="news"),
    url(r'^reviews/', views.ReviewView.as_view(), name="reviews"),
    url(r'^contacts/', views.contacts, name="contacts"),
]
