from django.test import TestCase

from car_washes.models import CarWashes
from car_washes.tests.factories import CarWashesFactory


class CarWashesModelTests(TestCase):

    def setUp(self):
        self.car_wash = CarWashesFactory()

    def test_car_washes_create__when_fields_are_valid__expect_success(self):
        self.assertIsNotNone(self.car_wash.pk)

    def test_car_washes_str_method__when_name_is_correct__expect_equal(self):
        self.assertEqual(str(self.car_wash), self.car_wash.car_wash_name)

    def test_car_washes_str_method__when_name_is_incorrect__expect_not_equal(self):
        self.assertNotEqual(str(self.car_wash), 'Some name')
