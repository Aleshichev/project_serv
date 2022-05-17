from django.db import models


# Create your models here.
from scraping.utils import from_cyrillic_to_eng


class City(models.Model):    # наследуемся с models для Sql
    """создали класс на основе модели джанго """
    name = models.CharField(max_length=50,
                            verbose_name='Название населённого пункта',
                            unique=True)    # поле с ограниченым колличеством символов unique - уникальное
    slug = models.CharField(max_length=50, blank=True, unique=True)      # blank=True поле может быть пустым

    class Meta:
        verbose_name = 'Название населённого пункта'
        verbose_name_plural = 'Название населённых пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)  # поле с ограниченым колличеством символов unique - уникальное
    slug = models.CharField(max_length=50, blank=True, unique=True)  # blank=True поле может быть пустым

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансий')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город' )
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования' )
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'

    def __str__(self):
        return self.title