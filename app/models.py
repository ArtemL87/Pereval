from django.db import models


class User(models.Model):
    email = models.CharField(unique=True, max_length=50)
    fam = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    otc = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{fam} {name} {otc}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    height = models.IntegerField()

    def __str__(self):
        return f'Широта - {latitude}, долгота - {longitude}, высота - {height}'


class Level(models.Model):
    difficulty_category = [
        (None, '--'),
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б')
    ]

    winter = models.CharField(max_length=2, choices=difficulty_category, default=None)
    summer = models.CharField(max_length=2, choices=difficulty_category, default=None)
    autumn = models.CharField(max_length=2, choices=difficulty_category, default=None)
    spring = models.CharField(max_length=2, choices=difficulty_category, default=None)

    def __str__(self):
        return f'Сложность перевала:\nЗимой - {winter}\nЛетом - {summer}\nОсенью - {autumn}\nВесной - {spring}'


class PerevalAdd(models.Model):
    message_status = [
        ('new', 'Попало в очередь на модерацию'),
        ('pending', 'Модератор взял в работу'),
        ('accepted', 'Модерация прошла успешно, информация принята'),
        ('rejected', 'Модерация прошла, информация не принята'),
    ]

    status = models.CharField(max_length=50, choices=message_status, default='new')
    beauty_title = models.CharField(max_length=10, default='пер. ')
    title = models.CharField(max_length=30)
    other_titles = models.CharField(max_length=30, blank=True, null=True)
    connect = models.CharField(max_length=2, default='')
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    image = models.ForeignKey('Image',on_delete=models.CASCADE)


class Image(models.Model):
    element_pereval = [
        (None, '-------'),
        ('1', 'Вершина'),
        ('2', 'Седловина'),
        ('3', 'Хребет'),
        ('4', 'Обрыв'),
        ('5', 'Терраса'),
        ('6', 'Лощина'),
        ('7', 'Водораздел'),
        ('8', 'Склон'),
    ]
    title_image = models.CharField(max_length=30, choices=element_pereval)
    date_added = models.DateTimeField(auto_now_add=True)
    data = models.ImageField()

# Create your models here.
