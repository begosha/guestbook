from django import forms

from webapp.models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'email', 'booking_details', 'status')


class GuestDeleteForm(forms.Form):
    name = forms.CharField(max_length=1000, required=True, label='Enter the name to delete')
