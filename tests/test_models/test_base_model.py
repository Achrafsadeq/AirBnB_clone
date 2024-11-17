#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        self.model = BaseModel()

    def test_basic_attributes(self):
        """Test if basic attributes are set correctly"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_to_dict(self):
        """Test conversion to dictionary"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_from_dict(self):
        """Test creation from dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertIsNot(self.model, new_model)


if __name__ == '__main__':
    unittest.main()
