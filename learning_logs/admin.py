from atexit import register
from django.contrib import admin

# imports the model we want to register, Topic
# the do in front og models tells Django to look for models.py 
# in the same directory as admin.py
from .models import Topic, Entry

# tells Django to manage our model through the admin site 
admin.site.register(Topic)              # 
admin.site.register(Entry) 