# Generated by Django 2.0 on 2018-07-26 10:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zascat', '0011_auto_20180725_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrepCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категори',
            },
        ),
        migrations.AlterField(
            model_name='prep',
            name='prep_date',
            field=models.DateField(default=datetime.datetime(2018, 7, 26, 10, 21, 24, 265740, tzinfo=utc), verbose_name='Дата добавления (изменения)'),
        ),
        migrations.AlterField(
            model_name='prep',
            name='prep_eng_name',
            field=models.CharField(max_length=50, verbose_name='Наименование препарата по английски для красивого URL'),
        ),
        migrations.AddField(
            model_name='prep',
            name='prep_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='zascat.PrepCategory'),
        ),
    ]