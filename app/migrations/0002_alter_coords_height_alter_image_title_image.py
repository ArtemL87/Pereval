# Generated by Django 4.2.1 on 2023-05-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coords',
            name='height',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='image',
            name='title_image',
            field=models.CharField(choices=[(None, '-------'), ('1', 'Вершина'), ('2', 'Седловина'), ('3', 'Хребет'), ('4', 'Обрыв'), ('5', 'Терраса'), ('6', 'Лощина'), ('7', 'Водораздел'), ('8', 'Склон')], max_length=30),
        ),
    ]
