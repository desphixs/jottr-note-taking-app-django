from django.db import models

# Create your models here.
# A Django Model is like a blueprint or template for a database table.
# Think of it like a blank spreadsheet form: it defines what columns
# we want in our table so every new note (row) we add has the exact same structure!

# We define a class named "Note" that inherits from "models.Model".
# This inheritance tells Django that this class is not just a regular Python class,
# but a database model that should be translated into an actual database table.
class Note(models.Model):
    # The 'title' field represents the short heading of our note.
    # We use models.CharField (Character Field), which is perfect for short pieces of text.
    # Think of this like the "Subject" line of an email or the title of a folder.
    # We limit it to a maximum of 200 characters using max_length=200.
    title = models.CharField(max_length=200)

    # The 'content' field will store the actual bulk body of our note.
    # We use models.TextField here, which is designed for long-form, multi-line text.
    # Think of this like the large blank space on a notebook page where you can write
    # paragraphs of thoughts, lists, or code snippets without worrying about running out of space!
    content = models.TextField()

    # The 'created_at' field will record the exact date and time the note was created.
    # We use models.DateTimeField and set auto_now_add=True.
    # Think of this like a helpful postmark machine that automatically stamps the exact
    # date and time onto the note the moment it is saved, so we don't have to record it manually!
    created_at = models.DateTimeField(auto_now_add=True)

    # The '__str__' method is a special built-in Python method.
    # It controls how this note object is displayed as a simple string.
    # Instead of showing something generic like "<Note object (1)>", we want it to display
    # the note's actual title. This makes managing notes in the admin panel extremely intuitive!
    # Think of it like writing a clear label on the outside of a file folder so you know what is inside.
    def __str__(self):
        # We return the title of the note so it displays beautifully and readably.
        return self.title
