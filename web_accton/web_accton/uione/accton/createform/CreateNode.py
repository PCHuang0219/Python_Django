from django import forms

class NodeForm(forms.Form):
    Node_name = forms.CharField(label='Node Name', max_length=100)

