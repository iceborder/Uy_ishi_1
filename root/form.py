from django.forms import ModelForm
from root.models import Forms


class ContactForm(ModelForm):

    class Meta:
        model = Forms
        fields = '__all__'
