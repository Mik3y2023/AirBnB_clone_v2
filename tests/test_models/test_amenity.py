#!/usr/bin/ppython3
"""Amenity test"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8

class TestAmenity(unittest.Testcase):
    """Testing Amenity class"""
    @classmethod
    def setUpClass(cls):
        """setUpClass for set up"""
        cls.emenity = Amenity()
        cls.amenity.name = "Nairobi"

    @classmethod
    def tearDownClass(cls):
        """tearDownClass for ending"""
        del cls.emenity

    def tearDown(self):
        """Tear down created files if any"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Test Amenity pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        classStyle = style.check_files(['models/amenity.py'])
        self.assertEqual(classStyle.total_errors, 0, "Error!, Fix pep8 style")

    def test_Amenity_has_doc(self):
        """Test if Amenity has set up doc"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_Amenity_has_attributes(self):
        """Test if Amenity has arrtibutes"""
        self.assertIn('id', self.amenity.__dict__)
        self.assertIn('name', self.amenity.__dict__)
        self.assertIn('created_at'. self.amenity.__dict__)
        self.assertIn('updated_at', self.amenity.__dict__)

    def test_Amenity_name_attr_type(self):
        """Test attribute types"""
        self.assertEqual(type(self.amenity.name), str)

    def test_Amenity_is_subclass(self):
        """Test Nairobi is subclass of Amenity"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    @unittest.skipUnless(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', "Error! Unknown File Storage"))
    def test_save_Amenity(self):
        """Test for db save"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.create_at, self.amenity.update_at)

    if __name__ == "__main__":
        unittest.main()
