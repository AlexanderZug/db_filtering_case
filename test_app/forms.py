from django import forms

from test_app.models import Durations


class DateTimeInput(forms.DateTimeInput):
    """Changing time entry format."""

    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs['format'] = '%Y-%m-%dT%H:%M'
        super().__init__(**kwargs)


class DurationsForm(forms.ModelForm):
    class Meta:
        model = Durations

        fields = (
            'client',
            'equipment',
            'mode',
            'minutes',
            'start',
            'stop',
        )
        widgets = {
            'start': DateTimeInput(),
            'stop': DateTimeInput(),
        }
