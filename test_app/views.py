from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from test_app.forms import DurationsForm
from test_app.models import Durations


class IndexView(CreateView):
    form_class = DurationsForm
    template_name = 'index.html'
    success_url = reverse_lazy('test_app:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Durations.objects.select_related('equipment', 'client', 'mode').all()
        return context
#
# class IndexView(ListView):
#     model = Durations
#     queryset = Durations.objects.select_related('equipment', 'client', 'mode').all()
#     template_name = 'index.html'
#     context_object_name = 'page_obj'
