from django.db import models

# Create your models here.
class Sender (models.Model):
    from_name = models.CharField('От кого', max_length=50)
    from_index = models.IntegerField(verbose_name='Индекс отправителя', null=True)
    from_street = models.CharField('Адрес, начиная с улицы', max_length=254)
    from_region = models.CharField('Страна, Регион, Область', max_length=254)
    from_email = models.EmailField(null=True)

    class Meta:
        verbose_name = u'Отправитель'
        verbose_name_plural = u'Отправители'

    def __str__(self):
        return self.from_name

class Reciever (models.Model):
    to_name = models.CharField('Кому', max_length=50)
    to_index = models.IntegerField(verbose_name='Индекс Получателя', null=True)
    to_street = models.CharField('Адрес, начиная с улицы', max_length=254)
    to_region = models.CharField('Адрес, начиная с улицы', max_length=254)
    to_email = models.EmailField(null=True)

    class Meta:
        verbose_name = u'Получатель'
        verbose_name_plural = u'Получатели'

    def __str__(self):
        return self.to_name