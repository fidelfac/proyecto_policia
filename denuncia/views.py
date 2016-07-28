from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from .models import Denuncia



from django.template import loader

def mostrar(request):
    
    return render(request, 'denuncia/add.html')

class IndexView(generic.ListView):
    template_name = 'denuncia/index.html'
    context_object_name = 'latest_denuncia_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Denuncia.objects.order_by('-motivo')[:5]

class AddView(generic.ListView):

	template_name = 'denuncia/add.html'
#def index(request):
    #return HttpResponse("hola")
