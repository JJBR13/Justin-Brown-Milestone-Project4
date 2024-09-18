from django import forms
from .widgets import CustomClearableFileInput
from .models import TourProducts, Category, TourImage

class TourForm(forms.ModelForm):

    class Meta:
        model = TourProducts
        fields = '__all__'

    image = forms.ImageField(
        label='Update Tour Image', 
        required=False, 
        widget=CustomClearableFileInput(attrs={'class': 'form-control-file', 'initial_text': 'Update Tour Image'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

class TourImageForm(forms.ModelForm):
    class Meta:
        model = TourImage
        fields = ['image']
