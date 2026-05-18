from django.shortcuts import render
# We import 'HttpResponse' from django.http to demonstrate how to send raw text back to the browser.
# In professional apps, writing full HTML code inside Python strings is incredibly messy and disorganized!
# That is why we quickly graduate to using the 'render' function, which loads a separate, clean HTML template.
from django.http import HttpResponse

# We import our Note model blueprint class from our local models.py file
from .models import Note

# Create your views here.
# In Django, a "view" is just a standard Python function that takes a web request and returns a web response.
# Think of a view function like a friendly restaurant chef: when a customer submits an order (a web request),
# the chef prepares the meal (fetches and processes data) and sends the finished plate back to the table (the response)!
def note_list(request):
    # We fetch all the notes stored inside our SQLite database cabinet using Django's ORM!
    # Think of 'Note.objects.all()' like the chef opening the Notes cabinet drawer,
    # pulling out every single folder registered inside, and loading them onto our serving tray!
    # This returns a QuerySet, which acts exactly like a list of Note model objects.
    notes_data = Note.objects.all()

    # We pack our database records into a central dictionary called 'context'.
    # Think of the context dictionary like a physical serving tray: we load our database notes
    # onto this tray under the label key 'notes', so the waiter (render function)
    # can carry the tray out to the dining area (index.html template) for the user!
    context = {
        'notes': notes_data,
    }

    # We call the render function and pass our 'context' tray as the third argument!
    # Django will carry this database data to the index.html template, allowing us to loop
    # through the notes and display them dynamically!
    return render(request, 'notes/index.html', context)

# We define a brand new view function to serve the details page of a single specific note!
# In addition to the standard 'request' parameter, this function takes a second parameter: 'pk'.
# 'pk' stands for Primary Key, which is the unique cardboard tab ID stamped on each cabinet folder!
def note_detail(request, pk):
    # We fetch a single specific note folder from our filing cabinet using its unique Primary Key (pk)!
    # Think of 'Note.objects.get(pk=pk)' like the detective going directly to the folder with the exact ID stamp
    # and pulling it out of the drawer!
    note = Note.objects.get(pk=pk)

    # We pack our single database note record into a central context tray dictionary under the key 'note'.
    context = {
        'note': note,
    }

    # We call the render function to deliver the single note details to our new detail template!
    return render(request, 'notes/note_detail.html', context)
