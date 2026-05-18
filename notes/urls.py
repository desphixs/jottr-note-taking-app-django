# We import path from django.urls to define our app's specific route mappings.
from django.urls import path
# We import the views file from our current directory (represented by the dot '.') to access our view functions.
from . import views

# We define a variable called 'app_name' to namespace our routes.
# Think of this like giving our store its own unique brand name: it prevents Django from getting confused
# if another app in our shopping mall project has a route with the exact same name!
app_name = 'notes'

# The urlpatterns list holds all the active routes that belong specifically to our notes app.
# Think of this list like a specialized navigation signpost mounted right inside the notes store itself!
urlpatterns = [
    # This empty path '' maps directly to our 'note_list' view function.
    # When a visitor lands on the homepage of our notes section, Django will call the 'note_list' chef!
    # We assign name='note_list' so we can easily reference this path in our templates later.
    path('', views.note_list, name='note_list'),
]
