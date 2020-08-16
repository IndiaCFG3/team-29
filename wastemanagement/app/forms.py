from django.forms import ModelForm
from .models import Form1model

class Form1(ModelForm):
    class Meta:
        model = Form1model
        fields = ['name','location','vehicle_number','Quantity','num_trips','type_waste','image','comments']