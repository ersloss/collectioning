from django.forms import ModelForm

from collection.models import Collection
from crispy_forms.helper import FormHelper

class NewCollectionForm(ModelForm):

    def __init__(self):
        super(NewCollectionForm, self).__init__()
        self.helper = FormHelper(self)

    class Meta:
        model = Collection
        fields = ('name',)
