

# Create your views here.
# rental/views.py
from .forms import BookingForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Property
from .forms import PropertyForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listings')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



@login_required

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def home(request):
    return render(request, 'home.html')


# Add more views as needed
# rental/views.py


def listings(request):
    properties = Property.objects.all()
    new_property_id = request.GET.get('new_property_id')
    new_property = None

    if new_property_id:
        try:
            new_property = Property.objects.get(id=new_property_id)
        except Property.DoesNotExist:
            new_property = None

    return render(request, 'listings.html', {'properties': properties, 'new_property': new_property})

@login_required
def booking(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.property = property
            booking.save()
            messages.success(request, 'Your booking has been successfully submitted!')
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'property': property, 'form': form})