from django import forms

from test_app.models import Durations


class DateInput(forms.DateInput):
    input_type = 'date'


class DurationsForm(forms.ModelForm):
    class Meta:
        model = Durations
        widgets = {'start': DateInput(),
                   'stop': DateInput()}
        fields = ('client', 'equipment', 'mode', 'start',
                  'stop', 'minutes',)
