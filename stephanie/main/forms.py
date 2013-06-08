from django import forms

from . import models


class Contact(forms.ModelForm):

    class Meta:
        model = models.Contact
        exclude = ('sent', 'modified')
