from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PerevalAdd, User, Coords, Level, Image
from .serializers import PerevalAddSerializer, PerevalSerializer, PerevalUpdataSerializer

class PerevalModelsTests(APITestCase):
    def setUp(self):
        self.data = {
            "beauty_title": "пер. ",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",

            "add_time": "",
            "user": {"email": "qwerty@mail.ru",
                     "fam": "Пупкин",
                     "name": "Василий",
                     "otc": "Иванович",
                     "phone": "+7 555 55 55"},

            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},

            "level": {"winter": "1Б",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": "2А"},

            "image": {"data": None, "title_image": 3},
        }
        self.pereval = PerevalAdd.objects.create(
            beauty_title='Beauty1',
            title='Title 1',
            other_titles='Other1',
            connect='',
            user=User.objects.create(
                email='user1@mail.ru',
                fam='fam1',
                name='name1',
                otc='otc1',
                phone='+71111111111'
            ),
            coords=Coords.objects.create(
                latitude=11.11111,
                longitude=22.22222,
                height=1234
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1Б',
                autumn='2A',
                spring='2Б'
            ),
            image=Image.objects.create(title_image=1, data=None)
        )

    def test_create_pereval(self):
        url = reverse('new')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pereval(self):
        response = self.client.get(reverse('id', kwargs={'pk' : self.pereval.id}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

