from django.test import TestCase
from .models import Children

class ChildrenModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='Sani',
        email='saniibrahimvws1@gmail.com',
        password='abukar0202'
        )
    @classmethod
    def setUpTestData(cls):
        child.objects.create(registrar=self.user,
                                clinic='MCH',
                                ward='Gamboru Ward A',
                                card_number='1111111111',
                                firs_name='Ali',
                                certificate_number='2222222222',
                                mother_name='Halima',
                                father_name='Audu',
                                address='AB',
                                gender='Male'
                            )
def test_clinic_content(self):
    child = Children.objects.get(id=2)
    expected_object_name = f'{child.clinic}'
    self.assertEqual(expected_object_name, 'MCH')

def test_ward_content(self):
    Child = Children.objects.get(id=1)
    expected_object_name = f'{child.ward}'
    self.assertEqual(expected_object_name, 'Gamboru Ward A')

def test_card_content(self):
    child = Children.objects.get(id=1)
    expected_object_name = f'{child.card_number}'
    self.assertEqual(expected_object_name, '1111111111')

def test_name_content(self):
    child = Children.objects.get(id=1)
    expected_object_name = f'{child.firs_name}'
    self.assertEqual(expected_object_name, 'Aliyu')

def test_certificate_content(self):
    child = Children.objects.get(id=1)
    expected_object_name = f'{child.certificate_number}'
    self.assertEqual(expected_object_name, '2222222222')

def test_mother_content(self):
    child = Children.objects.get(id=1)
    expected_object_name = f'{child.mother_name}'
    self.assertEqual(expected_object_name, 'Halima')

def test_Father_content(self):
    child = Children.objects.get(id=1)
    expected_object_name = f'{child.father_name}'
    self.assertEqual(expected_object_name, 'Audu')

def test_address_content(self):
    Child = Children.objects.get(id=1)
    expected_object_name = f'{child.address}'
    self.assertEqual(expected_object_name, 'AB')


def test_gender_content(self):
    Child = Children.objects.get(id=1)
    expected_object_name = f'{child.body}'
    self.assertEqual(expected_object_name, 'Male')
