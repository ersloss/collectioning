from django.forms import ModelForm

from collection.models import Collection


class NewCollectionForm(ModelForm):

    def __init__(self):
        super(NewCollectionForm, self).__init__()

    class Meta:
        model = Collection
        fields = ('name',)
