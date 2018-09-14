from django import forms

from .models import Question, Choice

from django.forms.models import inlineformset_factory


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text',)


class TextForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
