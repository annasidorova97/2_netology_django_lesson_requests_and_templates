from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_view(request):
    context = {
        'test': 5,
        'data': [1, 5, 8, 12],
        'val': 'hello'
    }
    return render(request, 'demo.html', context)


def sum_view(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f'Sum = {result}')