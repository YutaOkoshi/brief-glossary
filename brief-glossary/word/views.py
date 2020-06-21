from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Word


class IndexView(generic.ListView):
    template_name = 'word/index.html'
    paginate_by = 3
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five modified word."""
        return Word.objects.order_by('-modified')[:5]


class DetailView(generic.DetailView):
    model = Word
    template_name = 'word/detail.html'


class ResultsView(generic.DetailView):
    model = Word
    template_name = 'word/results.html'


class AddView(generic.DetailView):
    model = Word
    template_name = 'word/add.html'

# def vote(request, question_id):
#     question = get_object_or_404(Word, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'word/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('word:results', args=(question.id,)))
