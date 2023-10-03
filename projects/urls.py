from django.urls import path
from .views import ProjectDetailsView, ProjectListView

urlpatterns = [
    path("api", ProjectListView.as_view()),
    path("api/<int:project_id>/", ProjectDetailsView.as_view(),),
]