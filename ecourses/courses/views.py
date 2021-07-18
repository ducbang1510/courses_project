from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("e-Course App")
    return render(request, template_name='index.html', context={
        'name': 'Duc Bang'
    })
