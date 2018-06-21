from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .tasks import proc_file


class IndexView(generic.View):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        """
        We can process the file during get if we want to.
        In case, just uncomment the method bellow
        """
        #proc_file.delay()
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        """
        Process the file when the user click in the button
        """
        proc_file.delay()
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