from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    #return HttpResponse("hi")
    context = {'username': 'Cat'}
    return render_to_response('index.html', context, context_instance = RequestContext(request))

    