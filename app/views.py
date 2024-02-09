from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse

class templatehtml(TemplateView):
    template_name='templatehtml.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Deepali'
        ECDO['age']=3
        return ECDO
    
class insert_schoolby_tv(TemplateView):
    template_name='insert_schoolby_tv.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert School by Template view is done')
        
class insert_schoolby_fv(FormView):
    template_name='insert_schoolby_fv.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('insert school by form view is done')
