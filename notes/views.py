from django.shortcuts import render
# We import 'HttpResponse' from django.http to demonstrate how to send raw text back to the browser.
# In professional apps, writing full HTML code inside Python strings is incredibly messy and disorganized!
# That is why we quickly graduate to using the 'render' function, which loads a separate, clean HTML template.
from django.http import HttpResponse

# Create your views here.
# In Django, a "view" is just a standard Python function that takes a web request and returns a web response.
# Think of a view function like a friendly restaurant chef: when a customer submits an order (a web request),
# the chef prepares the meal (fetches and processes data) and sends the finished plate back to the table (the response)!
def note_list(request):
    # We define a Python list of dictionaries containing our dummy note data.
    # Think of this list like a temporary inventory list written on the chef's clipboard
    # before we build the official database filing cabinet. Each dictionary is a separate card!
    notes_data = [
        {
            # Each note card has key-value pairs representing its attributes:
            'title': 'First Test Note',
            'content': 'Welcome to Jottr! This is a dynamic dummy note passed straight from our view function context dictionary to make sure our template loops work beautifully.',
            'created_at': 'Just Now',
            'tag': 'Welcome',
            'color': 'blue'
        },
        {
            'title': 'Buy Groceries',
            'content': 'Remember to purchase organic milk, farm-fresh brown eggs, whole wheat sourdough bread, and fresh rosemary for dinner cooking.',
            'created_at': '1 Hour Ago',
            'tag': 'Shopping',
            'color': 'purple'
        },
        {
            'title': 'Next Big Startup',
            'content': 'Build an AI-powered automated code mentor that reads plans and writes highly clean, beginner-friendly explanations of complex tech stacks step-by-step!',
            'created_at': 'Yesterday',
            'tag': 'Ideas',
            'color': 'amber'
        }
    ]

    # We pack our inventory list into a central dictionary called 'context'.
    # Think of the context dictionary like a physical serving tray: we load our raw notes
    # onto this tray under a custom label key 'notes', so the waiter (render function)
    # can carry the tray out to the dining area (index.html template) for the user!
    context = {
        'notes': notes_data,
    }

    # We call the render function and pass our 'context' tray as the third argument!
    # Django will carry this data to the index.html template, allowing us to loop
    # through the notes and display them dynamically!
    return render(request, 'notes/index.html', context)
