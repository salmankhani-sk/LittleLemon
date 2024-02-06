# Create a file in the restaurant directory called forms.py and import the following:  

# The Booking model from the file models.py.

# The module forms from the package django
from django import forms
from myapp.forms import BookingForm

from restaurant import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name
    
# Still inside the forms.py file, create a class called BookingForm and pass the forms.ModelForm as an argument to it. 
# Inside the class BookingForm, create another class called Meta and declare the following attributes inside it:  
    
# Model with the value Booking  

# Field with the value "__all__"

class BookingForm(forms.ModelForm):
        
        class Meta:
            model = BookingForm
            fields = '__all__'
