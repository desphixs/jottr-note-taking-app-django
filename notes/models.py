from django.db import models

# Create your models here.
# In Django, a "Model" represents a structured blueprints of a database table.
# Think of a model class like a physical blueprint template used to organize a filing cabinet:
# each class is a new drawer in the cabinet (a table), and each attribute inside the class
# defines a specific file tab or label column (a database column)!
class Note(models.Model):
    # The title field represents the main header of our sticky note.
    # We use a CharField (Character Field) because titles are short text strings.
    # We enforce max_length=200 so users don't type a whole novel as their title!
    title = models.CharField(
        max_length=200,
        help_text="The main heading for your sticky note card."
    )    
    # The content field holds the main detailed description body of the note.
    # We use a TextField because it is designed to store long-form, multi-line paragraph text.
    content = models.TextField(
        help_text="The rich details and descriptions of your thoughts."
    )
    
    # The created_at field records the exact calendar timestamp when the note is created.
    # We use a DateTimeField with auto_now_add=True, which instructs Django:
    # "The absolute moment this note gets saved to the filing cabinet, grab the current
    # system date and time, stamp it, and lock it in forever so we never have to set it manually!"
    created_at = models.DateTimeField(auto_now_add=True)

    # The __str__ method defines how Python represents our Note object as a string.
    # Think of this like labeling the physical folder tab inside the drawer:
    # instead of Django showing a generic "Note object (1)" in our admin screen,
    # it will print the actual title of the note so we can easily search and identify it!
    def __str__(self):
        return self.title
