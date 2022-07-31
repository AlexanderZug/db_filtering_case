from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from test_app.forms import DurationsForm
from test_app.models import Durations
from test_app.utils import (result_to_output_all_data,
                            result_to_output_without_day,
                            result_to_output_without_hour)


class IndexView(CreateView):
    form_class = DurationsForm
    template_name = 'index.html'
    success_url = reverse_lazy('test_app:index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        query = Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query(instance)
        month = Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_month(instance)
        day = Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_day(instance)
        if query:
            messages.success(self.request, result_to_output_all_data(query))
        elif day:
            messages.success(self.request, result_to_output_without_hour(day))
        elif month:
            messages.success(self.request, result_to_output_without_day(month))
        return HttpResponseRedirect(reverse('test_app:index'))
