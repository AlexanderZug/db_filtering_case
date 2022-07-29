import operator
from functools import reduce

from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from test_app.forms import DurationsForm
from test_app.models import Durations


class IndexView(CreateView):
    form_class = DurationsForm
    template_name = 'index.html'
    success_url = reverse_lazy('test_app:index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        bd_filter = Durations.objects.select_related(
            'equipment', 'client', 'mode'
        ).filter(
            reduce(operator.and_, (Q(client=instance.client),))
            | reduce(operator.and_, (Q(equipment=instance.equipment),))
            | reduce(operator.and_, (Q(mode=instance.mode),))
            | reduce(operator.and_, (Q(minutes=instance.minutes),))
            | reduce(operator.and_, (Q(start=instance.start),))
            | reduce(operator.and_, (Q(stop=instance.stop),))
        )
        result = ''
        for i in bd_filter:
            result += f'{i.client} {i.equipment} {i.mode} {i.minutes} {i.start} {i.stop}<br>'
        messages.success(self.request, result)
        return HttpResponseRedirect(reverse('test_app:index'))
