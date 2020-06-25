# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
from django.views import generic

from .models import Word


class IndexView(generic.ListView):
    template_name = 'word/index.html'
    paginate_by = 3
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Word.objects.order_by('-modified')[:5]

    # def get_context_data(self):
    #     context = super().get_context_data(**data)
    #     context["bar"] = Word._meta.get_fields()
    #     fields =
    #     return


class DetailView(generic.DetailView):
    model = Word
    template_name = 'word/detail.html'


class DeleteView(generic.DetailView):
    model = Word
    template_name = 'word/delete.html'


class AddView(generic.DetailView):
    model = Word
    template_name = 'word/add.html'
