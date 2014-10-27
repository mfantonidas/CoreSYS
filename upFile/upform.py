from django import forms
from bootstrap_toolkit.widgets import BootstrapTextInput

class UpForm(forms.Form):
    filename = forms.CharField(required=True, label=u"月份", error_messages={'required':u'月份'}, widget=forms.TextInput(attrs={'placeholder':u"月份", 'class':"form-control",}),)
    dutyfile = forms.FileField()