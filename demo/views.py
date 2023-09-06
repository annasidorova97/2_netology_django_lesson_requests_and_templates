from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_view(request):
    name = request.GET.get('name', 'Vasya')  # работает, как со словарем по ключу name, если нет name, то вернется Vasya
    age = int(request.GET['age'])  # сработает только если задан в запросе параметр age=n
    return HttpResponse(f'Hello {name}')


def sum_view(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f'Sum = {result}')