# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# def test(request, id=None):
def test(request, **kwargs):
    id = kwargs['id']
    value = request.GET.get('name')
    return HttpResponse('OK, id={}, val={}\n'.format(id, value))
