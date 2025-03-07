from django.urls import path

from organizations import views

urlpatterns = [
    path("organizations/", views.OrganizationViewSet.as_view({"get": "list"}), name="organizations-list"),
]
