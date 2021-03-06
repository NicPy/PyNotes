from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import  auth
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .forms import AddNoteForm, AddCategoryForm
from django import forms
from django.http import HttpResponse

from .models import Note, Category


# Create your views here.


# @login_required()
def index(request):
    # user = get_object_or_404(User)

    if not request.user.is_authenticated:
        username = request.user.username
        return redirect('login_view')
    
    else:

        if request.method == 'POST' and 'add_note' in request.POST:
            initial = {'pub_author': request.user.id,
                       'note_text': request.POST['note_text'].replace("\n\r", "<hr />"),
                       }
            print(request.POST['note_text'])
            print("--------------------------------------------------------------------------")


            form = AddNoteForm(request.POST or None, initial = initial )
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect('/notes/')

        if request.method == 'POST' and 'add_category' in request.POST:

            category_form = AddCategoryForm(request.POST or None)
            if category_form.is_valid():
                category_form.save()
                return redirect('/notes/')

        else:
            user = request.user

            initial = {'pub_author': request.user.id}
            form = AddNoteForm(request.POST or None, initial=initial)
            category_form = AddCategoryForm(request.POST or None)
            latest_notes_list = Note.objects.filter(pub_author = user).order_by('-pub_date')[:12]
            categories = Category.objects.order_by('id')





            context = {'latest_notes_list': latest_notes_list,
                       'form': form,
                       'category_form': category_form,
                       'categories': categories,
                       # 'cat-posts': get_notes(),
                       # 'username': username,

                       }
            return render(request, 'index.html', context)


def detail(request, note_id):
    # if request.method == 'POST':
    #     instance = SomeModel.objects.get(id=id)
    #     instance.delete()
    note = get_object_or_404(Note, pk=note_id)
    print(note.note_text)
    return render(request, 'detail.html', {'note': note})

def note_remove(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('/notes/')

def signup(request):
    if request.user is not None:  # and user.is_active:
        return redirect("/notes")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('/notes/', {'username': username })
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    auth.logout(request)

    return redirect('/notes/')
def login_view(request):
    #

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None: # and user.is_active:
            auth.login(request, user)
            return redirect("/notes")
    # if request.user is not None:  # and user.is_active:
        # return redirect("/notes")
    else:
        if request.user is not None:  # and user.is_active:
            return redirect("/notes")
        return render(request, "login_form.html")


def log_in(request):
    username = auth.get_user(request).username
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password=password)
    print('________________________________________')
    print(' It is it')
    print('________________________________________')
    # if user is not None:
    #     if user.is_active:
    #         login(request, user)
    #         # Redirect to a success page.
    #     else:
    #         # Return a 'disabled account' error message
    #         ...
    # else:
    #     # Return an 'invalid login' error message.
    #     ...
    return HttpResponse
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def add_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

def get_search(request):
    if request.is_ajax():
        import json
        q = request.GET.get('term', '')
        data_for_search = Note.objects.filter(note_heading__icontains=q)[:20]
        results = []
        for data in data_for_search:
            data_json = {}
            data_json['id'] = data.id
            data_json['label'] = data.note_heading
            data_json['value'] = data.note_heading
            results.append(data_json)
        final_data = json.dumps(results)
    else:
        final_data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(final_data, mimetype)

def search(request):
    if request.GET['search']:
        q = request.GET['search']
        posts = Note.objects.filter(pub_author = request.user, note_heading__icontains=q) | \
                Note.objects.filter(pub_author = request.user, note_text__icontains=q)
                # Note.objects.filter(pub_author = request.user, category__icontains=q)
        return render(request, 'results.html', {'posts':posts, 'q':q})
    else:
        return render(request, 'index.html')

#     # try:
#     #     note_title = question.choice_set.get(pk=request.POST['note_title'])
#     #     note_text = question.choice_set.get(pk=request.POST['note_text'])
#     # except (KeyError, Note.DoesNotExist):
#     #     # Redisplay the question voting form.
#     #     return render(request, 'polls/detail.html', {
#     #         'question': question,
#     #         'error_message': "You didn't select a choice.",
#     #     })
#     # else:
#     #     selected_choice.votes += 1
#     #     selected_choice.save()
#     #     # Always return an HttpResponseRedirect after successfully dealing
#     #     # with POST data. This prevents data from being posted twice if a
#     #     # user hits the Back button.
#     #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
