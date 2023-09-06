from django.core.paginator import Paginator
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


CONTENT = [str(i) for i in range(10000)]


def paginator_view(request):
    page_number = int(request.GET.get('page', 1))
    pagi = Paginator(CONTENT, 10)
    page = pagi.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'paginator.html', context)
