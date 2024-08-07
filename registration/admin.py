from django.contrib import admin
from django.utils.html import format_html
from .models import Booking, Guest

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_details', 'guests', 'alert_phone_number', 'pending_final')

    def booking_details(self, obj):
        return format_html('<strong>{}</strong><br>{}', obj.name, obj.school_email)

    def guests(self, obj):
        guests = obj.guests.all()
        guest_details = "<br>".join(
            [f"{guest.name} ({guest.email})" for guest in guests]
        )
        return format_html(guest_details)

    booking_details.short_description = 'Booking Details'
    guests.short_description = 'Guests'

admin.site.register(Booking, BookingAdmin)
admin.site.register(Guest)
