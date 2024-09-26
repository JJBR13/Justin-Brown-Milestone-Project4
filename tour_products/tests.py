from django.test import TestCase
from .models import Category

class CategoryModelTests(TestCase):
    """ Test case for the Category model """

    def setUp(self):
        """ Create a sample Category instance to use in tests """
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Friendly Test Category'
        )

    def test_string_representation(self):
        """ Test the __str__ method of the Category model """
        self.assertEqual(str(self.category), 'Test Category')

    def test_get_friendly_name(self):
        """ Test the get_friendly_name method of the Category model """
        self.assertEqual(self.category.get_friendly_name(), 'Friendly Test Category')

    def test_verbose_name_plural(self):
        """ Test the verbose name plural of the Category model """
        self.assertEqual(str(Category._meta.verbose_name_plural), 'Categories')

    def test_category_without_friendly_name(self):
        """ Test creating a category without a friendly name """
        category = Category.objects.create(name='No Friendly Name')
        self.assertIsNone(category.get_friendly_name())

