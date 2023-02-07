from django.test import TestCase
from .models import PerevalUser
from .models import Coords
from .models import Image 
from .models import Pereval
from django.test import Client

# Create your tests here.

class submitDataTest(TestCase):
    def setUp(self):
        self.user = PerevalUser.objects.create(phone = '+77777777777',
                                               email = 'user@example.com',
                                               firstname = 'firstname',
                                               lastname = 'lastname',
                                               middlename = 'middlename')
                                               
        self.coords = Coords.objects.create(latitude = 61.7096,
                                            longitude = 59.5418,
                                            height = 1000)
        
        self.images = [Image.objects.create(title = 'image title',
                                          data = 'image data'),]

        self.pereval = Pereval.objects.create(user = self.user,
                                              status = 'ne',
                                              title = 'pereval title',
                                              other_titles = 'other perevel title',
                                              beautyTitle = 'beauty pereval title',
                                              coords = self.coords,
                                              connect = 'none',
                                            #   images = self.images,
                                              winter = '',
                                              summer = '',
                                              autumn = '',
                                              spring = ''
                                              )
        self.pereval.save()

    def tearDown(self) -> None:
        self.user.delete()
        self.pereval.delete()
        self.coords.delete()

    def test_read_pereval(self):
        self.assertEqual(self.pereval.user, self.user)
        self.assertEqual(self.pereval.title, 'pereval title')

    def test_update_pereval_title(self):
        self.pereval.title = 'new pereval title'
        self.pereval.save()
        self.assertEqual(self.pereval.title, 'new pereval title')
    
    # def test_get(self):
    #     client = Client()
    #     response = client.get(f'/submitData/{self.pereval.pk}')

    def test_post(self):
        client = Client()
        data = {
                    "title": "string",
                    "other_titles": "string",
                    "beautyTitle": "string",
                    "connect": "string",
                    "status": "ne",
                    "user": {
                        "phone": "+77777777755",
                        "email": "newuser4@example.com",
                        "firstname": "string",
                        "lastname": "string",
                        "middlename": "string"
                    },
                    "coords": {
                        "latitude": 0,
                        "longitude": 0,
                        "height": 2147483647
                    },
                    "images": [
                        {
                        "data": "string",
                        "title": "string"
                        }
                    ],
                    "winter": "1a",
                    "spring": "1a",
                    "summer": "1a",
                    "autumn": "1a"
                }
        response = client.post('/submitData/', data)
        print(response.content)
        self.assertEqual(response.status_code, 201)
