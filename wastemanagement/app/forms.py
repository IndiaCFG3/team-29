from django.forms import ModelForm
from .models import Form1model

class Form1(ModelForm):
    class Meta:
        model = Form1model
        #fields = "__all__"
        fields = ['name','location','vehicle_number','quantity','num_trips','type_waste','image','comments']