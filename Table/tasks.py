import requests

from PeopleTable.celery import app
from Table.models import People, AgeGroup
from Table.services import append_peoples_db, append_age_group_db


@app.task
def get_people_data():
    """Отправка get запроса для получения данных о людях"""
    response = requests.get('https://6297558514e756fe3b2d94ed.mockapi.io/api/v1/People').json()
    append_peoples_db(response)
    return get_age_group_data()


@app.task
def get_age_group_data():
    """Отправка get запроса для получения данных о возрастных группах"""
    response = requests.get('https://6297558514e756fe3b2d94ed.mockapi.io/api/v1/AgeCroup').json()
    append_age_group_db(response)
    return set_relation()


@app.task
def set_relation():
    """Устанавливает связь между People и AgeGroup"""
    all_peoples = People.objects.all()
    all_groups = AgeGroup.objects.all()

    for people in all_peoples:
        for group in all_groups:
            if people.age > 5 and group.age_from < people.age < group.age_to:
                group_object = AgeGroup.objects.get(id=group.id)
                people.group = group_object
                people.save()
