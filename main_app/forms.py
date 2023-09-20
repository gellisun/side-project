from django.forms import ModelForm
from .models import Exhibition

class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = ['name', 'closingDate', 'description', 'feedback']
    
    def __init__(self, *args, **kwargs):
        super(ExhibitionForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Exhibition name'
        self.fields['closingDate'].widget.attrs['placeholder'] = 'MM/DD/YYYY'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe the exhibition here...'
        self.fields['feedback'].widget.attrs['placeholder'] = 'Give your feedback about the exhibition...'