#!/usr/bin/python3
"""BaseModel test"""
import os
import unittest
import pep8
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """setUpClass for BaseModel test"""
        cls.base = BaseModel()
        cls.base.name = "Bojack"
        cls.base.num = 44

    @classmethod
    def tearDownClass(cls):
        """tearDownClass for BaseModel test"""
        del cls.base

    def test_del_files_BaseModel(self):
        """Test to del created files if any"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        classStyled = style.check_files(['models/base_model.py'])
        self.assertEqual(classStyled.totalErrors, 0, "Error!, Fix pep8 style")

    def test_BaseModel_has_necessary_functions(self):
        """Test if the functions exists"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "__repr__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_BaseModel_has_doc(self):
        """Check if BaseModel has docs"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__repr__.__doc__)

    def test_is_type_of_BaseModel(self):
        self.assertTrue(isInstance(self.base, BaseModel))

    @unittest.skip("Checking if it works")
    def test_nothing(self):
        self.fail("ERROR!, This shouldn't be seen")

if __name__ == "__main__":
    unittest.main()
