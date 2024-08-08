from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking, Guest

def book_tickets(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            number_of_tickets = form.cleaned_data.get('number_of_tickets')

            for i in range(1, number_of_tickets):
                guest_name = request.POST.get(f'guest_name_{i}')
                guest_email = request.POST.get(f'guest_email_{i}')
                if guest_name and guest_email:
                    Guest.objects.create(booking=booking, name=guest_name, email=guest_email)

            return redirect('success')
        else:
            return render(request, 'booking/book_tickets.html', {'form': form})

    else:
        form = BookingForm()

    return render(request, 'booking/book_tickets.html', {'form': form})

def success(request):
    return render(request, 'booking/success.html')