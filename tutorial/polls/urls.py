from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/new_Question', views.NewQuestionView.as_view(), name='newQuestion'),
    path('polls/new_Choice/', views.NewChoiceView.as_view(), name='newChoice'),
    path('polls/<int:pk>/delete_question', views.DeleteQuestionView.as_view(), name='deleteQuestion'),
    path('polls/<int:pk>/edit_question', views.EditQuestionView.as_view(), name='editQuestion'),
    path('polls/<int:pk>/list_choice', views.DetailChoiceView.as_view(), name='listChoice'),
    path('polls/<int:pk>/delete_choice', views.DeleteChoiceView.as_view(), name='deleteChoice'),
    path('polls/<int:pk>/edit_choice', views.EditChoiceView.as_view(), name='editChoice'),

]