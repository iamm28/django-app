from django.urls import path, re_path
from howdy import views

urlpatterns = [
    re_path(r'^$', views.HomePageView.as_view()),
    re_path(r'^about/$', views.AboutPageView.as_view()),
]
