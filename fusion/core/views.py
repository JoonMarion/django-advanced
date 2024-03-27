from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Servicos, Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context


class View404(TemplateView):
    template_name = '404.html'
