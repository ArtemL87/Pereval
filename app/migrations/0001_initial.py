# Generated by Django 4.2.1 on 2023-05-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.CharField(choices=[(None, '-------'), ('1', 'Вершина'), ('2', 'Седловина'), ('3', 'Хребет'), ('4', 'Обрыв'), ('5', 'Терраса'), ('6', 'Лощина'), ('7', 'Водораздел'), ('8', 'Склон'), ('9', 'Подъем'), ('10', 'Спуск')], max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('data', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[(None, '--'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default=None, max_length=2)),
                ('summer', models.CharField(choices=[(None, '--'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default=None, max_length=2)),
                ('autumn', models.CharField(choices=[(None, '--'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default=None, max_length=2)),
                ('spring', models.CharField(choices=[(None, '--'), ('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default=None, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('fam', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('otc', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Попало в очередь на модерацию'), ('pending', 'Модератор взял в работу'), ('accepted', 'Модерация прошла успешно, информация принята'), ('rejected', 'Модерация прошла, информация не принята')], default='new', max_length=50)),
                ('beauty_title', models.CharField(default='пер. ', max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('other_titles', models.CharField(blank=True, max_length=30, null=True)),
                ('connect', models.CharField(default='', max_length=2)),
                ('add_time', models.TimeField(auto_now_add=True, null=True)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coords')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
