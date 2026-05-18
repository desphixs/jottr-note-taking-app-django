from django.contrib import admin
# We need to import our Note model from the models.py file in the current folder.
# The single dot '.' means "look in the current folder" (which is the notes app folder).
from .models import Note

# Register your models here.
# By registering the Note model, we are officially telling Django's Admin panel:
# "Please display our Note model on the administrator dashboard so we can create,
# view, update, and delete note entries using a beautiful, pre-built web interface!"
# Think of this like adding a custom store management panel on the manager's master desktop.
admin.site.register(Note)
