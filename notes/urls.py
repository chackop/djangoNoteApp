from django.urls import path

from . import views

urlpatterns = [
    # path("notes", views.test_notes),
    # path("note/<int:pk>", views.test_detail),
    # path("notes", views.NotesListView.as_view()),
    # path("notes/<int:pk>", views.NotesDetailView.as_view()),
    path("notes", views.NotesListView.as_view(), name="notes.list"),
    path("notes/<int:pk>", views.NotesDetailView.as_view(), name="notes.detail"),
    path("notes/new", views.NotesCreateView.as_view(), name="notes.new"),
    path("notes/<int:pk>/edit", views.NotesUpdateView.as_view(), name="notes.update"),
    path("notes/<int:pk>/delete", views.NotesDeleteView.as_view(), name="notes.delete"),
]
