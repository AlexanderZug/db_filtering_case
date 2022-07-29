from django import forms

from test_app.models import Durations


class DurationsForm(forms.ModelForm):
    class Meta:
        model = Durations
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     MYQUERY = Durations.objects.all()
    #     self.fields['myfield'] = forms.ChoiceField(choices=(*MYQUERY,))