from django import forms
from .models import Note
from django.contrib.auth.models import User



class AddNoteForm(forms.ModelForm):

    class Meta:

        model = Note

        fields = [
            'note_heading',
            'note_text',
            'pub_date',
            'pub_author'
        ]
        widgets = {
            'note_heading': forms.TextInput(attrs={'class': 'col-md-12'}),

            'note_text': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'col-md-12'}),
            'pub_author': forms.HiddenInput()
        }



        #
        # def set_value(dict):
        #     Meta.widgets[dict[0]] = forms.HiddenInput(attrs={'value' :dict[1]})
