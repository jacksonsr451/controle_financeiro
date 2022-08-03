from unittest import TestCase
import unittest

from flask import Flask

from app import app


class TestGetAllDespesas(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app()
        
    
    def test_if_app_instance_of(self):
        self.assertIsInstance(self.app, Flask)

