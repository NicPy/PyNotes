from django import forms
from .models import Note, Category
from django.contrib.auth.models import User



class AddNoteForm(forms.ModelForm):

    class Meta:

        model = Note

        fields = [
            'note_heading',
            'note_text',
            'note_category',
            'pub_date',
            'pub_author'
        ]
        widgets = {
            'note_heading': forms.TextInput(attrs={'class': 'col-md-12 form-control'}),


            'note_text': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'col-md-12 form-control'}),
            'pub_date': forms.TextInput(attrs={'class': 'form-control date'}),
            'note_category': forms.Select(attrs={'class': 'form-control date' }),
            'pub_author': forms.HiddenInput()
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =[
            'name',
        ]
        labels = {
            "name": ""
        }
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control primary-font', 'placeholder': 'Add new folder'}),

        }
        #
        # def set_value(dict):
        #     Meta.widgets[dict[0]] = forms.HiddenInput(attrs={'value' :dict[1]})
