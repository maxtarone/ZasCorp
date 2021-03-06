# Generated by Django 2.0 on 2019-04-04 07:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zascat', '0016_auto_20190403_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepcategory',
            name='cat_hfu',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Название английскими буквами для понятного URL без пробелов'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prep',
            name='prep_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 4, 7, 56, 25, 223559, tzinfo=utc), verbose_name='Дата добавления (изменения)'),
        ),
    ]
