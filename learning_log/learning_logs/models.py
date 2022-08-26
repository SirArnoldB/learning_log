from cgitb import text
from tabnanny import verbose
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about.
    
    The Topic class inherits from Model.

    Attributes:
        text:
            CharField instance. The name of the topic.
        date_added:
            DateTimeField instance. The date and time the topic was created.
    
    Methods:
        __str__(self):
            Displays a simple representation of the Topic model
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic.
    
    The entry class inherits from Django's base Model class.
    Each entry will be associated with a particular toipic in a 
    many-to-one relationship (many entries can be associated with one topic).

    Attributes:
        topic: 
            ForeignKey instance. Connects each entry to a specific topic.
        text: 
            TextField instance. Individual entry text.
        date_added: 
            Allows ordering entries, and placing of a timestamp next to each entry.
    
    Classes:
        Meta:
            Sets an attribute telling Django to use Entries when it needs to refer to 
            more than one entry.
    
    Method:
        __str__(self):
            Tells Django which information to show when referring to individual entries.
            Shows the first 50 characters of text, and an ellipsis to clarify that we;re not always
            displaying the entire entry.
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else f"{self.text}"