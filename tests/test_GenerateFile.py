import unittest
import sys
import tempfile
sys.path.insert(1, "..")
from setupPython.GenerateFile import GenerateFile
from setupPython.SetupData import SetupData


class test_GenerateFile(unittest.TestCase):

    def setUp(self):
        self.generateFile = GenerateFile()
        self.setupData = SetupData()
    
    def test_generateFileWithCorrectData(self):
        utilityName = "MyUtilityTest"
