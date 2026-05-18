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

    # This dynamic path maps to our 'note_detail' view function.
    # The segment '<int:pk>/' acts like a smart mail filter: it checks the URL path for an integer
    # (like /1/ or /2/) and captures it as a variable named 'pk' to pass directly to our chef!
    path('<int:pk>/', views.note_detail, name='note_detail'),

    # This path maps to our 'create_note' view function to handle sticky note submissions.
    # When a visitor clicks "New Sticky Note", they land on '/new/' and see our beautiful note form!
    path('new/', views.create_note, name='create_note'),

    # This path maps to our 'edit_note' view function to handle editing existing notes.
    # The segment '<int:pk>/edit/' captures the barcode ID of the note being updated,
    # and opens a pre-populated workspace for edit operations!
    path('<int:pk>/edit/', views.edit_note, name='edit_note'),

    # This path maps to our 'delete_note' view function to handle deleting existing notes.
    # The segment '<int:pk>/delete/' captures the barcode ID of the note being deleted,
    # and opens a confirmation dialog warning screen!
    path('<int:pk>/delete/', views.delete_note, name='delete_note'),
]
