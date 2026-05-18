from django.shortcuts import render, redirect
# We import 'HttpResponse' from django.http to demonstrate how to send raw text back to the browser.
# In professional apps, writing full HTML code inside Python strings is incredibly messy and disorganized!
# That is why we quickly graduate to using the 'render' function, which loads a separate, clean HTML template.
from django.http import HttpResponse

# We import our Note model blueprint class from our local models.py file
from .models import Note
# We import our newly designed NoteForm class from our local forms.py file
from .forms import NoteForm

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

# We define a brand new view function to handle note creation!
# Think of this view function like a two-way street or a post-office counter:
# 1. When a user first opens the page (GET request), we hand them a fresh, clean, empty note form (blank letter).
# 2. When they click submit (POST request), we collect their typed text package, check it, and save it!
def create_note(request):
    # We check if the incoming request method is a POST submission (user sent a package!)
    if request.method == 'POST':
        # We fill our note form plaster mold with the raw data packages sent inside the request!
        form = NoteForm(request.POST)

        # We verify if the data passed all validation checks (e.g. not empty, correct formats)
        if form.is_valid():
            # If the mold is verified valid, we save the new note directly to our SQLite database!
            form.save()
            # We redirect the visitor cleanly back to our homepage dashboard!
            # Think of 'redirect' like a automatic portal redirecting their browser instantly!
            return redirect('notes:note_list')
    else:
        # If it is a GET request, the user is just loading the page for the first time.
        # We hand them a fresh, empty NoteForm plaster mold!
        form = NoteForm()

    # We pack our active form plaster mold onto our central context serving tray!
    context = {
        'form': form,
    }

    # We call the render function and deliver our form serving tray to the create_note template!
    return render(request, 'notes/create_note.html', context)

# We define a brand new view function to handle editing existing sticky notes!
# Just like note_detail, this view takes both 'request' and 'pk' parameters.
# 'pk' represents the unique cardboard tab barcode ID of the note being updated!
def edit_note(request, pk):
    # We fetch the specific note folder we want to edit from our SQLite database cabinet!
    note = Note.objects.get(pk=pk)

    # We check if the incoming request is a POST submission (user clicked "Save Changes"!)
    if request.method == 'POST':
        # We fill our note form mold, but this time we pass two arguments:
        # 1. 'request.POST' representing the new edited text packages.
        # 2. 'instance=note' pointing back to our existing database row record!
        # Think of this like replacing the content inside the exact same cardboard folder rather than creating a new one!
        form = NoteForm(request.POST, instance=note)

        # We verify if the updated fields pass our validation checks
        if form.is_valid():
            # We save the modified mold, which updates the existing SQLite row!
            form.save()
            # Once updated, we redirect the browser straight to the note's own detail page!
            return redirect('notes:note_detail', pk=note.pk)
    else:
        # If it is a GET request, the user is loading the edit screen for the first time.
        # We initialize our NoteForm mold pre-filled with the existing note details using 'instance=note'!
        form = NoteForm(instance=note)

    # We pack the active pre-filled form mold and the note record onto our serving tray!
    context = {
        'form': form,
        'note': note,
    }

    # We render the edit_note.html template and deliver the context serving tray!
    return render(request, 'notes/edit_note.html', context)

# We define a brand new view function to handle deleting existing notes!
# This view takes both 'request' and 'pk' parameters to capture the targeted note card!
def delete_note(request, pk):
    # We fetch the specific note folder we want to delete from our SQLite database cabinet!
    note = Note.objects.get(pk=pk)

    # We check if the incoming request is a POST submission (user confirmed deletion!)
    if request.method == 'POST':
        # We delete the note folder permanently from our database cabinet!
        note.delete()
        # Once deleted, we redirect the user cleanly back to our homepage note dashboard!
        return redirect('notes:note_list')

    # If it is a GET request, the user is just loading the delete confirmation screen!
    # We pack the note object onto our serving tray so the template can show a preview of what is being deleted!
    context = {
        'note': note,
    }

    # We render our delete confirmation workspace template!
    return render(request, 'notes/delete_note.html', context)
