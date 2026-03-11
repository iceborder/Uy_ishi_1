from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from root.form import ContactForm
from root.models import Fields, Forms


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Fields'] = Fields.objects.all()
        context['Forms'] = Forms.objects.all()
        return context


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return str(reverse_lazy('index')) + '#contact'
