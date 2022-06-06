import json

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import People
from .services import get_peoples_order_by, get_peoples_by_start_from, get_peoples
from .tasks import get_people_data


def get_data(request):
    """Запустить цепочку задач в Celery для получения данных"""
    get_people_data.apply_async()
    response = {'status': 'ok'}
    return JsonResponse(response, safe=False)


def table_page(request):
    """Страница с таблицей людей"""
    all_peoples = get_peoples()
    return render(request, 'Table/table.html', locals())


def get_peoples_data(request):
    """Функция возвращает JSON людей"""
    all_peoples = get_peoples()
    response = []
    for people in all_peoples:
        response.append({'name': people.name, 'age': people.age, 'group': people.group.group_name})
    json.dumps(response)
    return JsonResponse(response, safe=False)


def filter_name(request):
    """Функция фильтрации по имени"""
    all_peoples = get_peoples_order_by('name')
    response = []
    for people in all_peoples:
        response.append({'name': people.name, 'age': people.age, 'group': people.group.group_name})
    json.dumps(response)
    return JsonResponse(response, safe=False)


def filter_age(request):
    """Функция фильтрации по возрасту"""
    all_peoples = get_peoples_order_by('-age')
    response = []
    for people in all_peoples:
        response.append({'name': people.name, 'age': people.age, 'group': people.group.group_name})
    json.dumps(response)
    return JsonResponse(response, safe=False)


def search_by_name(request):
    """Функция поиска по имени"""
    if request.method == 'POST':
        peoples = get_peoples_by_start_from('name', request.POST.get('name').capitalize())
        response = []
        if peoples:
            for people in peoples:
                response.append({'name': people.name, 'age': people.age, 'group': people.group.group_name})
            json.dumps(response)
        return JsonResponse(response, safe=False)


def search_by_age(request):
    """Функция поиска по возрасту"""
    if request.method == 'POST':
        peoples = get_peoples_by_start_from('age', request.POST.get('age'))
        response = []
        for people in peoples:
            response.append({'name': people.name, 'age': people.age, 'group': people.group.group_name})
        json.dumps(response)
        return JsonResponse(response, safe=False)


def handler_404(request, exception):
    return redirect('table_page')
