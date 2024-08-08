from django.contrib import admin
from .models import Booking, Guest

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 0
    readonly_fields = ('name', 'email')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'school_email', 'number_of_tickets', 'alert_phone_number', 'pending_final')
    inlines = [GuestInline]

admin.site.register(Booking, BookingAdmin)
admin.site.register(Guest)