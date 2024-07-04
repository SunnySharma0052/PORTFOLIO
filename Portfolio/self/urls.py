from django.contrib import admin
from django.urls import path
from self import views

urlpatterns = [
    path("", views.Navbar, name="Base"),
    path("Project/", views.Project, name="Project"),
    path("About/", views.About, name="About"),
    path("Contact/", views.Contact_form, name="Contact"),
]
