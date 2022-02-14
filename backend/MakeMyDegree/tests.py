from django.test import TestCase
from MakeMyDegree.models import *


class AppTestCase(TestCase):
    def setUp(self):
        test_degree = Degree.objects.create(
            degree_type="BS",
            degree_name="Computer Engineering",
            school="ECE",
            term="Fa2019"
        )

        User.objects.create(
            name="Jude Lei",
            password="graphsRox",
            email="lei56@purdue.edu",
            degree=test_degree,
            curr_plan={}
        )

    def test_create_user(self):
        test_user = User.objects.get(name="Jude Lei")
        self.assertEqual(test_user.email, "lei56@purdue.edu")
        self.assertNotEqual(test_user.degree.school, "CE")
