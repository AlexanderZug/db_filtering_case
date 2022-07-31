from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from test_app.forms import DurationsForm
from test_app.utils import (result_to_output_all_data,
                            result_to_output_without_day,
                            result_to_output_without_hour,
                            filtered_time_query_set,
                            result_to_output_without_month,
                            result_to_output_without_year)


class IndexView(CreateView):
    form_class = DurationsForm
    template_name = 'index.html'
    success_url = reverse_lazy('test_app:index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        query = filtered_time_query_set()['query'](instance)
        if query:
            messages.success(self.request, result_to_output_all_data(query))
        elif filtered_time_query_set()['hour'](instance):
            messages.success(self.request, result_to_output_without_hour(filtered_time_query_set()['hour'](instance)))
        elif filtered_time_query_set()['day'](instance):
            messages.success(self.request, result_to_output_without_day(filtered_time_query_set()['day'](instance)))
        elif filtered_time_query_set()['month'](instance):
            messages.success(self.request, result_to_output_without_month(filtered_time_query_set()['month'](instance)))
        elif filtered_time_query_set()['year'](instance):
            messages.success(self.request, result_to_output_without_year(filtered_time_query_set()['year'](instance)))
        return HttpResponseRedirect(reverse('test_app:index'))
