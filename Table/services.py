from Table.models import AgeGroup, People


def append_peoples_db(response):
    """Добавляет всех полученных людей в модель People"""
    peoples = [People(name=data.get('name'),
                      birth_day=data.get('birth_day'),
                      birth_month=data.get('birth_month'),
                      age=data.get('age')) for data in response]
    People.objects.bulk_create(peoples)


def append_age_group_db(response):
    """Добавляет все полученные возрастные группы в модель AgeGroup"""
    age_groups = [AgeGroup(age_from=data.get('age_from'),
                           age_to=data.get('age_to'),
                           group_name=data.get('group_name')) for data in response]
    AgeGroup.objects.bulk_create(age_groups)


def get_peoples():
    return People.objects.filter(group__isnull=False)


def get_peoples_order_by(order_by):
    """Функция принимает поле, по котором нужно сделать order_by и возвращает QuerySet людей, у которых есть группа"""
    return People.objects.filter(group__isnull=False).order_by(order_by)


def get_peoples_by_start_from(start_from, start_from_data):
    """Функция принимает название поля (start_from), по которому будет искать начинающиеся значение (data) """
    if start_from == 'age':
        return People.objects.filter(group__isnull=False, age__startswith=start_from_data)
    elif start_from == 'name':
        return People.objects.filter(group__isnull=False, name__startswith=start_from_data)

