from django import forms
from .models import Zamowienie

class ZamownienieForm(forms.ModelForm):
    
    class Meta:
        model = Zamowienie
        exclude = ['data']
        widgets = {
            'data_usługi': forms.SelectDateWidget(),
            'data_urodzenia': forms.SelectDateWidget(),
            'data_śmierci': forms.SelectDateWidget(),
            'komentarz': forms.Textarea()
        }
