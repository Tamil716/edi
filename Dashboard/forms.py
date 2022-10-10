from django import forms

class ContactForm(forms.Form):
    title=forms.CharField();
    content=forms.CharField(widget=forms.Textarea)