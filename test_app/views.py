
from django.contrib import messages
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
        ).filter(client=instance.client, equipment=instance.equipment,
                 mode=instance.mode, minutes=instance.minutes,
                 start__year=instance.start.date().year, stop__year=instance.stop.date().year,
                 start__month=instance.start.date().month, stop__month=instance.stop.date().month,
                 start__day=instance.start.date().day, stop__day=instance.stop.date().day,
                 start__hour=instance.start.time().hour, stop__hour=instance.stop.time().hour,
        )
        if bd_filter:
            result = ''
            for i in bd_filter:
                result += (f'{i.client} {i.equipment} {i.mode} {i.minutes} '
                           f'{i.start.strftime("%m/%d/%Y, %H")} '
                           f'{i.stop.strftime("%m/%d/%Y, %H")}<br> ')
            messages.success(self.request, result)
        else:
            messages.success(self.request, '!')
            return HttpResponseRedirect(reverse('test_app:index'))
        return HttpResponseRedirect(reverse('test_app:index'))
