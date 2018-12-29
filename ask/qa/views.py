# from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
# from django.db import connection
from django.contrib.auth.models import User


def index(request):
    users = User.objects.all()
    # cur = connection.cursor()
    # a = cur.execute('select * from auth_user')
    # return render(request, 'index.html')
    return HttpResponse('OK, a={}'.format(users[0].get_username()))


# def test(request, **kwargs):
def test(request, id=None):
    # id = kwargs['id']
    value = request.GET.get('name')
    return HttpResponse('OK, id={}, val={}\n'.format(id, value))
