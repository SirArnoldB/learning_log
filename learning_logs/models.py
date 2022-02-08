from tabnanny import verbose
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""

    # topic is a ForeignKey instance. 
    # a foreign key is a database term; it's a reference to another record in the database
    # This is the code that connects each entry to a specific topic. 
    # Each topic is assigned a key, or ID, when it’s created. When Django needs to establish a connection
    # between two pieces of data, it uses the key associated with each piece of information. 
    # We’ll use these connections shortly to retrieve all the entries associated with a certain topic. 
    # The on_delete=models.CASCADE argument tells Django that when a topic is deleted, all the entries associated with that topic should be deleted as well. 
    # This is known as a cascading delete
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # text is an instance of TextField
    # and does not have a size limit because we do not want to limit the size of the individual entries 
    # the date_attribute allows us to present entries in the order they were created and to place a timestamp to each entry 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # the Meta class holds extra information for managing a model; 
    # Here; it allows us to set a special attribute telling Django to use Entries when it needs to refer to more than one entry
    # Without this, Django would refer to multiple entries as Entrys. 
    class Meta:
        verbose_name_plural = 'entries'
    
    # The __str__() method tells Django which information to show when it refers to individual entries. 
    # Because an entry can be a long body of text, we tell Django to show just the first 50 characters of text
    def __str__(self) -> str:
        """Return a string representation of the model."""
        # we also add an ellipsis to clarify that we're not always displaying the entire entry 
        return f"{self.text[:50]}..."
