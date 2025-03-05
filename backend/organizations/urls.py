from django.urls import path

from . import views

urlpatterns = [
    path("organizations/", views.OrganizationViewSet.as_view({"get": "list"}), name="organizations-list"),
    path("organizations/<int:pk>/", views.OrganizationViewSet.as_view({"get": "retrieve"}), name="organizations-detail"),
    path("news/", views.NewsViewSet.as_view({"get": "list"}), name="news-list"),
    path("news/<int:pk>/", views.NewsViewSet.as_view({"get": "retrieve"}), name="news-detail"),
]
