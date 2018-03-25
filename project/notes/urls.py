from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^note/(?P<pk>\d+)/remove/$', views.note_remove, name='note_remove'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    # url(r'^login_form', )
    url(r'^api/get_search/', views.get_search, name='get_search'),
    url(r'^search/$', views.search, name='search'),


    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/add_note/', views.add_note, name='add_note'),

]