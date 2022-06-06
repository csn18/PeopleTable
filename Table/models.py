from django.db import models


class AgeGroup(models.Model):
    """
    Модель для хранения возрастных групп людей
    """
    age_from = models.IntegerField()
    age_to = models.IntegerField()
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'


class People(models.Model):
    """
    Модель для хранения информации о людях
    """
    name = models.CharField(max_length=255)
    birth_day = models.IntegerField()
    birth_month = models.IntegerField()
    age = models.IntegerField(null=True)
    group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
