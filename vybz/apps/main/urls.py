from django.urls import path 
from django.views.generic import TemplateView
from . import views

app_name = "main"

urlpatterns = [
    path("home/", TemplateView.as_view(template_name="main/home.html"), name="test_page"),
    path("test/", TemplateView.as_view(template_name="base.html"), name="test_page"),
    path("", views.HomePageView.as_view(), name="home_page_view"),

]
