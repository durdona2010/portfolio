from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'email', 'subject', 'message']

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if not firstname:
            raise forms.ValidationError("First name is required.")
        if len(firstname) < 3:
            raise forms.ValidationError("First name must be at least 3 characters.")
        return firstname

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise forms.ValidationError("Subject is required.")
        return subject

    