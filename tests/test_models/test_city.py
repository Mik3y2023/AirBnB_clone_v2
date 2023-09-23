#!/usr/bin/python3
"""Test for City Class"""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test for the City class"""

    @classmethod
    def setUpClass(cls):
        """setUpClass for City test class"""
        cls.city = City()
        cls.city.name = "Nairobi City"
        cls.city.state_id = "Nairobi"

    @classmethod
    def tearDownClass(cls):
        """Tears down created test class obj"""
        del cls.city

    def test_del_city_files(self):
        """Test to del created city files if any"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_for_City(self):
        """Test for pep8 style"""
        style = pep8.styleGuide(quiet=true)
        classStyled = style.check_files(['models/city.py'])
        self.assertEqual(classStyled.total_errors, 0,  "Error!, Fix pep8 style")

    def test_City_has_docs(self):
        """Test for City docs"""
        self.assertIsNotNone(City.__doc__)

    def test_City_has_attrs(self):
        """Test for attributes in City"""
        self.assertIn('id', self.city.__dict__)
        self.assertIn('name', self.city.__dict__)
        self.assertIn('state_id', self.city.__dict__)
        self.assertIn('create_at', self.city.__dict__)
        self.assertIn('updated_at', self.city.__dict__)

    def test_is_City_subclass(self):
        """Test City is BaseModel subsclass"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), true)

    def test_attributes_types_in_City(self):
        """Test attributes types in City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE') != 'db'"),
                         "Error! Unknown File Storage")

    def test_City_save(self):
        """Test if save works"""
        self.city.save()
        self.assertNotEqual(self.city.create_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()
