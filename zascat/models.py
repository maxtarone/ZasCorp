from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill


# Create your models here.


class PrepCategory(models.Model):
    name = models.CharField(u'Наименование категории', max_length=50)
    img = models.ImageField(u'Картинка для категори', upload_to='%Y/%m/%d/%H/%M/%S/')
    text = RichTextField(u'Описание категори', max_length=200)
    cat_hfu = models.CharField(u'Название английскими буквами для понятного URL без пробелов', max_length=50)

    class Meta:
        verbose_name = u'Категория препарата'
        verbose_name_plural = u'Категори препаратов'

    def __str__(self):
        return self.name


class Prep(models.Model):
    prep_is_active = models.BooleanField(u'Активен', default=True)
    prep_name = models.CharField(u'Наименование препарата', max_length=50)
    prep_preview_contains = models.CharField(u'Состав для предпоказа', max_length=200)
    prep_preview_desc = RichTextField(u'Описание для предпоказа')
    prep_date = models.DateField(u'Дата добавления (изменения)', default=timezone.now())
    prep_desc = models.CharField(u'Краткое описание (изготовитель, состав...)', max_length=254)
    prep_header = models.CharField(u'Заглавный лозунг', max_length=50)
    prep_category = models.ForeignKey(PrepCategory, null=True, blank=True,
                                      related_name='category', on_delete=models.CASCADE)
    prep_advert = RichTextField(u'Краткое рекламное описание', null=True)
    prep_apply_why = RichTextField(u'Для чего и где применять')
    prep_result = RichTextField(u'Действие и результат')
    prep_apply_how = RichTextField(u'Как применять')
    prep_eco_safe = RichTextField(u'Безопасность и экология')
    prep_package_table = RichTextField(u'Таблица фасовок')
    prep_eng_name = models.CharField(u'Наименование препарата по английски для красивого URL', max_length=50)
    prep_preview_image = models.ImageField(upload_to='%Y/%m/%d/%H/%M/%S/', null=True)

    class Meta:
        verbose_name = u'Препарат'
        verbose_name_plural = u'Препараты'

    def __str__(self):
        return self.prep_name


class PrepImages(models.Model):
    base_img = models.ImageField(upload_to='%Y/%m/%d/%H/%M/%S/')
    img_middle = ImageSpecField(source='base_img',
                                processors=[ResizeToFit(420, 420, mat_color='white')],
                                format='PNG')
    img_small = ImageSpecField(source='base_img',
                               processors=[ResizeToFit(270, 320, mat_color='white')],
                               format='PNG')
    prep = models.ForeignKey(Prep, on_delete=models.CASCADE, related_name='item', default='1')

    class Meta:
        verbose_name = u'Изображение препарата'
        verbose_name_plural = u'Изображения препарата'

    def __str__(self):
        return self.prep.prep_name


class PrepDocs(models.Model):
    doc_file = models.FileField(u'Файл для загрузки', upload_to='doc/%Y/%m/%d/%H/%M/%S/')
    doc_desc = models.CharField(u'Название документа', max_length=150)
    prep_name = models.ForeignKey(Prep, on_delete=models.CASCADE, related_name='document', null=True)

    class Meta:
        verbose_name = u'Документ препарата'
        verbose_name_plural = u'Документы препарата'

    def __str__(self):
        return self.prep_name.prep_name
