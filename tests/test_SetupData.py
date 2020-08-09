import unittest
import sys
sys.path.insert(1, "..")
from setupPython.SetupData import SetupData


class test_SetupData(unittest.TestCase):

    def setUp(self):
        self.setupData = SetupData()
    
