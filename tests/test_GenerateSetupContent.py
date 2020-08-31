import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.ContentTemplate import ContentTemplate
from tests.helpers import getPreparedSetupDate, getPreparedSetupDateWithoutEntryPoint
from tests.Mocking import Mocking


class test_GenerateSetupContent(unittest.TestCase):

    def setUp(self):
        self.generateSetupContent = GenerateSetupContent()

    def test_setContentTemplateFluentInterface(self):
        contentTemplate = ContentTemplate()
        returnedObject = self.generateSetupContent.setContentTemplate(contentTemplate)
        self.assertTrue(isinstance(returnedObject, GenerateSetupContent))

    def test_getContent(self):
        self.maxDiff = 10000

        contentTemplate = ContentTemplate().setSetupData(getPreparedSetupDate())

        self.generateSetupContent.setContentTemplate(contentTemplate)

        returnedContent = self.generateSetupContent.getContent()

        expected_content = Mocking().getFullSample()
        self.assertEqual(expected_content, returnedContent)

    def test_getContentWithoutEntryPoint(self):
        self.maxDiff = 10000

        contentTemplate = ContentTemplate().setSetupData(getPreparedSetupDateWithoutEntryPoint())
        self.generateSetupContent.setContentTemplate(contentTemplate)

        returnedContent = self.generateSetupContent.getContent()

        expected_content = Mocking().getSampleWithoutEntryPoint()
        self.assertEqual(expected_content, returnedContent)
