from django.forms import Form, CharField


class CardSearchForm(Form):
    query = CharField(max_length=100)
