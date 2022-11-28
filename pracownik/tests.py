from django.test import TestCase
from pracownik.forms import PracownikForm
from pracownik.models import Pracownik
# Create your tests here.

class PracownikTest(TestCase):

    def create_pracownik(self,imie="Jan", nazwisko="Kowalski", data_zatrudnienia="20.10.2021", wynagrodzenie = "10000",
                         rola="Tribe leader", data_urodzenia = "20.10.1974", econtact = "123123123", eemail= "test@test.pl" ):
        return Pracownik.objects.create( imie=imie, nazwisko = nazwisko, data_zatrudnienia = data_zatrudnienia, wynagrodzenie = wynagrodzenie,
                                        rola= rola, data_urodzenia = data_urodzenia, econtact = econtact, eemail = eemail )

    def test_pracownik_creation(self):
        w = self.create_pracownik()
        self.assertTrue(isinstance(w,Pracownik))
        self.assertEqual(w.__str__(), "3 Jan Kowalski")

class FormTest_valid(TestCase):
    def test_valid_form(self):
        p = Pracownik.objects.create(imie="Jan", nazwisko="Kowalski", data_zatrudnienia="20.10.2021", wynagrodzenie = "10000",
                         rola="Tribe leader", data_urodzenia = "20.10.1974", econtact = "123123123", eemail= "test@test.pl")
        data = { 'imie' :p.imie, 'nazwisko': p.nazwisko, 'data_zatrudnienia': p.data_zatrudnienia, 'wynagrodzenia': p.wynagrodzenie,
                 'rola': p.rola, 'data_urodzenia': p.data_urodzenia, 'econtact': p.econtact, 'eemail': p.eemail}
        form = PracownikForm(data= data)
        self.assertTrue(form.is_valid())

class FormTest_invaild(TestCase):

    def test_invalid_form(self):
        p = Pracownik.objects.create(imie="Jan", nazwisko="Kowalski", data_zatrudnienia="20.10.2021",
                                     wynagrodzenie="10000",
                                     rola="Tribe leader", data_urodzenia="20.10.1974", econtact="123123123",
                                     eemail="testtest.pl")
        data = {'imie': p.imie, 'nazwisko': p.nazwisko, 'data_zatrudnienia': p.data_zatrudnienia,
                'wynagrodzenia': p.wynagrodzenie,
                'rola': p.rola, 'data_urodzenia': p.data_urodzenia, 'econtact': p.econtact, 'eemail': p.eemail}
        form = PracownikForm(data=data)
        self.assertFalse(form.is_valid())