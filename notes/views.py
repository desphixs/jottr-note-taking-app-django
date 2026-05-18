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
    # Below is how we would return a simple raw string:
    # return HttpResponse("Welcome to Jottr! Your note-taking journey begins here.")
    #
    # However, to keep our code neat, professional, and scalable, we will immediately use the 'render' function.
    # This tells Django: "Go find a clean HTML file named 'index.html' inside the templates/notes directory,
    # combine it with any data we provide, and send it back to the visitor's screen!"
    # The first argument is the incoming request object, and the second is our template path.
    return render(request, 'notes/index.html')
