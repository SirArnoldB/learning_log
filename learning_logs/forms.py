from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    # nested Meta class tells Django which model to base the form on
    # and which fields to include in the form 
    class Meta:
        model = Topic
        fields = ['text']
        # do not generate a label for the text field 
        labels = {'text': ''}
    
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # give the field 'text' a blank label
        labels = {'text': 'Entry:'}
        # a widget is an HTML element 
        # including the widget attrivute overides Django's default widget choices 
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}