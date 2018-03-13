from django import forms
from .models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note

        fields = [
            'note_heading',
            'note_text',
            'pub_date',
        ]
        widgets = {
            'note_heading': forms.TextInput(attrs={'class': 'col-md-12'}),

            'note_text': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'col-md-12'}),
        }