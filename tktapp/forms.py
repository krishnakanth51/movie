from django import forms
from .models import Movies,Signup,Theatre,Booking

class Moviesform(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class Signupform(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class Loginform(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Theatreform(forms.ModelForm):
    class Meta:
        model = Theatre
        fields = '__all__'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date','showtime','ticketprice','name','select_seat']