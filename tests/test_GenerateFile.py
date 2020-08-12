import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateFile import GenerateFile
from setupPython.ContentTemplate import ContentTemplate
from setupPython.SetupData import SetupData

class test_GenerateFile(unittest.TestCase):

    def setUp(self):
        self.generateFile = GenerateFile()

    def test_setSetupDataFluentInterface(self):
        setupData = SetupData()
        returnedObject = self.generateFile.setSetupData(setupData)
        self.assertTrue(isinstance(returnedObject, GenerateFile))

    def test_setContentTemplateFluentInterface(self):
        contentTemplate = ContentTemplate()
        returnedObject = self.generateFile.setContentTemplate(contentTemplate)
        self.assertTrue(isinstance(returnedObject, GenerateFile))

