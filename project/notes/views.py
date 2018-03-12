from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Note

def index(request):
    latest_notes_list = Note.objects.order_by('-pub_date')[:3]
    context = {'latest_notes_list': latest_notes_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'note': note})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def add_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    # try:
    #     note_title = question.choice_set.get(pk=request.POST['note_title'])
    #     note_text = question.choice_set.get(pk=request.POST['note_text'])
    # except (KeyError, Note.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))