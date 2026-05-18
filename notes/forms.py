# We import forms from django to access the ModelForm base class
from django import forms
# We import our local Note database model class
from .models import Note

# We define a brand new Form class that inherits from forms.ModelForm
# Think of a ModelForm like an automated plaster cast mold: instead of building every input field manually,
# Django inspects our Note database table and builds the corresponding inputs automatically!
class NoteForm(forms.ModelForm):
    
    # The Meta class defines the settings and configurations for our plaster cast mold!
    class Meta:
        # We specify exactly which database table model this form is linked to
        model = Note
        
        # We specify exactly which fields we want the user to type inside our form inputs
        # (created_at is automatic and system-managed, so we exclude it!)
        fields = ['title', 'content']
        
        # We define customized widgets to control how each input field renders in HTML!
        # Think of widgets like designer custom outfits for our raw input boxes.
        # We pass high-end Tailwind styling classes directly into the 'class' attribute of each widget!
        widgets = {
            'title': forms.TextInput(attrs={
                # Highly styled Tailwind inputs: sleek gray bg, rounded borders, active Indigo rings!
                'class': 'w-full px-5 py-4 text-lg bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all duration-300 placeholder:text-slate-400 font-medium text-slate-800',
                # A friendly placeholder text guiding the student inside the input box
                'placeholder': 'Give your note a title...'
            }),
            'content': forms.Textarea(attrs={
                # Textarea has customized min-height and allows vertical scaling resizing
                'class': 'w-full px-5 py-4 text-base bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all duration-300 placeholder:text-slate-400 text-slate-600 min-h-[160px] resize-y',
                # A descriptive placeholder text guiding the student on what to write
                'placeholder': 'Type your thoughts or ideas here...'
            }),
        }
