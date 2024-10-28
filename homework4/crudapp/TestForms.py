from django.forms import ModelForm
from .models import Test

class Testform(ModelForm):
    class Meta:
        model = Test
        fields = ['test_field']