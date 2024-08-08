from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    school_email = models.EmailField()
    number_of_tickets = models.PositiveIntegerField()
    alert_phone_number = models.CharField(max_length=15)
    pending_final = models.FloatField(editable=False, default=0)

    def save(self, *args, **kwargs):
        if self.number_of_tickets % 2 == 0:
            pending = self.number_of_tickets * 5
        else:
            pending = self.number_of_tickets * 7
        self.pending_final = pending
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Guest(models.Model):
    booking = models.ForeignKey(Booking, related_name='guests', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.booking.name} - {self.name}'