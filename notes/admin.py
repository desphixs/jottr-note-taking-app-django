from django.contrib import admin

# We import our Note model blueprint class from the current app models file
from .models import Note

# Register your models here.
# In Django, the Admin site is a fully built-in visual database editor.
# By calling admin.site.register(Note), we instruct Django's management office:
# "Hey, display our Note table drawer inside the administrative dashboard panel!
# This grants us a gorgeous graphical user interface to create, read, update,
# and delete notes safely without writing SQL database queries by hand!"
admin.site.register(Note)
