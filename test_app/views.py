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
        res = Durations.filters_manager.db_query(instance)
        res_tree = Durations.filters_manager.db_query_time_month(instance)
        res_four = Durations.filters_manager.db_query_time_day(instance)
        res_two = Durations.filters_manager.db_query_time_hours(instance)
        if res and res_tree and res_four and res_two:
            print('!!')
            result = ''
            for i in res:
                result += (f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
                           f'| Minutes: {i.minutes} '
                           f'| Start: {i.start.strftime("%m/%d/%Y, %H")} '
                           f'| Stop: {i.stop.strftime("%m/%d/%Y, %H")}<br> ')
            messages.success(self.request, result)
        return HttpResponseRedirect(reverse('test_app:index'))
