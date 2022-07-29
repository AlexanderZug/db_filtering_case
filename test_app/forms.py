from django import forms

from test_app.models import Durations


class DurationsForm(forms.ModelForm):
    class Meta:
        model = Durations
        fields = ('client', 'equipment', 'mode', 'start',
                  'stop', 'minutes',)
