from django.db import models
status_choices = [('0', 'Blocked'), ('1', 'Active')]
class Guest(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Guest Name')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Guest E-mail')
    booking_details = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Booking Details')
    status = models.CharField(max_length=11, choices=status_choices, default=status_choices[1][1],verbose_name='Satus')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update Time')

    def __str__(self):

        return "{}. {}".format(self.pk, self.name)
