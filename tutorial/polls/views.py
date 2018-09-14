from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Choice, Question
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import QuestionForm, ChoiceForm, TextForm

from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    model = Question

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class NewQuestionView(CreateView):
    form_class = QuestionForm
    template_name = 'polls/new_question.html'
    success_url = reverse_lazy('polls:index')
    model = Question

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(NewQuestionView, self).form_valid(form)


class NewChoiceView(CreateView):
    form_class = ChoiceForm
    template_name = 'polls/edit_choice.html'
    model = Choice
    success_url = reverse_lazy('polls:index')


class DeleteQuestionView(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')


class EditQuestionView(UpdateView):
    form_class = QuestionForm
    template_name = 'polls/new_question.html'
    model = Question
    success_url = reverse_lazy('polls:index')

    def get_context_data(self, **kwargs):
        context = super(EditQuestionView, self).get_context_data(**kwargs)
        context['test'] = 'success'
        return context


class DetailChoiceView(generic.DetailView):
    model = Question
    template_name = 'polls/list_choice.html'


class DeleteChoiceView(DeleteView):
    model = Choice

    def get_success_url(self):
        return reverse_lazy('polls:listChoice', kwargs={'pk': self.object.question.pk})


class EditChoiceView(UpdateView):
    form_class = TextForm
    template_name = 'polls/edit_choice.html'
    model = Choice

    def get_success_url(self):
        return reverse_lazy('polls:listChoice', kwargs={'pk': self.object.question.pk})
