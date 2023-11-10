from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .forms import NotesForm
from .models import Notes
# Create your views here.


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = "/allnotes/notes"
    template_name = "notes/notes_delete.html"
    login_url = "/login"


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = "/allnotes/notes"
    form_class = NotesForm
    login_url = "/login"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = "/allnotes/notes"
    form_class = NotesForm
    login_url = "/login"

    # save with that user object
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    # displays notes just created by the user
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"


# def test_notes(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/testtemplate.html", {"notes": all_notes})


# def test_detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("This note doesn't exist")
#     return render(request, "notes/testtemplate.html", {"note": note})
