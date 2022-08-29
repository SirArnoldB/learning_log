from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Builds a form from the Topic model.
    
    The TopicForm class inherits from froms.ModelForm.
    """

    class Meta:
        """Specifies which model to base the form on, and which fields to include."""

        # Build a form from the Topic model
        model = Topic
        # Include only the text field
        fields = ['text']
        # Do not generate a label for the text field
        labels = {'text': ''}
    
class EntryForm(forms.ModelForm):
    """Builds an entry from the Entry model.
    
    The EntryForm class inherits from forms.ModelForm.
    """

    class Meta:
        """Specifies which model to base the entry on, and which fields to include."""

        # Build an entry from the Entry model
        model = Entry
        # Only include the text field in the form.
        fields = ['text']
        # Give the 'text' a blank label.
        labels = {'text': 'Entry:'}
        # Customize the input widget for the 'text' field.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}