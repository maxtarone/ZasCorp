from django.db import models
from django.utils import timezone


# Create your models here.

class PrepCategory(models.Model):
    name = models.CharField(u'Наименование категории', max_length=50)
    img = models.ImageField(u'Картинка для категори', upload_to='%Y/%m/%d/%H/%M/%S/')
    text = models.TextField(u'Описание категори', max_length=200)

    class Meta:
        verbose_name = u'Категория препарата'
        verbose_name_plural = u'Категори препаратов'

    def __str__(self):
        return self.name


class Prep(models.Model):
    prep_is_active = models.BooleanField(u'Активен', default=True)
    prep_name = models.CharField(u'Наименование препарата', max_length=50)
    prep_preview_contains = models.CharField(u'Состав для предпоказа', max_length=200)
    prep_preview_desc = models.TextField(u'Описание для предпоказа')
    prep_date = models.DateField(u'Дата добавления (изменения)', default=timezone.now())
    prep_desc = models.CharField(u'Краткое описание (изготовитель, состав...)', max_length=254)
    prep_header = models.CharField(u'Заглавный лозунг', max_length=50)
    prep_category = models.ForeignKey(PrepCategory, null=True, blank=True,
                                         related_name='category', on_delete=models.CASCADE)
    prep_advert = models.TextField(u'Краткое рекламное описание', null=True)
    prep_apply_why = models.TextField(u'Для чего и где применять')
    prep_result = models.TextField(u'Действие и результат')
    prep_apply_how = models.TextField(u'Как применять')
    prep_eco_safe = models.TextField(u'Безопасность и экология')
    prep_package_table = models.TextField(u'Таблица фасовок')
    prep_eng_name = models.CharField(u'Наименование препарата по английски для красивого URL', max_length=50)

    # TODO make "...|self" in template to parse html from all text.fields
    class Meta:
        verbose_name = u'Препарат'
        verbose_name_plural = u'Препараты'

    def __str__(self):
        return self.prep_name


class PrepImages(models.Model):
    src = models.ImageField(upload_to='%Y/%m/%d/%H/%M/%S/')
    prep = models.ForeignKey(Prep, on_delete=models.CASCADE, related_name='item', default='1')

    class Meta:
        verbose_name = u'Изображение препарата'
        verbose_name_plural = u'Изображения препарата'

    def __str__(self):
        return self.prep