from django import forms

from webapp.models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'email', 'booking_details')


