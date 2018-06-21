from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .tasks import proc_api


class IndexView(generic.View):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        """
        We can consume the API during get if we want to.
        In case, just uncomment the method bellow
        """
        #proc_api.delay()
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        """ 
        Execute the celery task since the user click the button
        """
        proc_api.delay()
        return render(request, self.template_name)


class Template404View(generic.TemplateView):
    '''
    Used to handle Page not Found error
    '''
    template_name = '404.html'


class Template500View(generic.TemplateView):
    '''
    Used to handle Server Error Page
    '''
    template_name = '500.html'
