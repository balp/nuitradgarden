# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from plants.models import Plant


class IndexView(generic.ListView):
    template_name = 'plants/index.html'
    model = Plant
    
    #def get_queryset(self, **kwargs):
    #    context = super(ArticleListView, self).get_context_data(**kwargs)
    #    return context


class DetailView(generic.DetailView):
    model = Plant
    template_name = 'plants/detail.html'
