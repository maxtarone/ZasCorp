# Generated by Django 2.0 on 2019-04-16 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zascat', '0020_auto_20190416_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrepDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='doc/%Y/%m/%d/%H/%M/%S/', verbose_name='Файл для загрузки')),
                ('doc_desc', models.CharField(max_length=150, verbose_name='Название документа')),
            ],
            options={
                'verbose_name': 'Документ препарата',
                'verbose_name_plural': 'Документы препарата',
            },
        ),
        migrations.AlterField(
            model_name='prep',
            name='prep_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 16, 13, 48, 57, 904178, tzinfo=utc), verbose_name='Дата добавления (изменения)'),
        ),
        migrations.AddField(
            model_name='prepdocs',
            name='prep_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document', to='zascat.Prep'),
        ),
    ]