from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from test_app.forms import DurationsForm
from test_app.utils import CheckQuerySet, filtered_time_query_set


class IndexView(CreateView):
    form_class = DurationsForm
    template_name = 'index.html'
    success_url = reverse_lazy('test_app:index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        for k, i in filtered_time_query_set().items():
            if i(instance):
                messages.success(
                    self.request,
                    CheckQuerySet(i(instance), k).get_output(),
                )
                break
        messages.error(self.request, 'Запрашиваемых данных не найдено')
        return HttpResponseRedirect(reverse('test_app:index'))
