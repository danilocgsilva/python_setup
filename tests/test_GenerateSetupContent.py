import unittest
import sys
sys.path.insert(1, "..")
import tempfile
import datetime
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.ContentTemplate import ContentTemplate
from tests.helpers import getPreparedSetupDate, getPreparedSetupDateWithoutEntryPoint, savePhysicallyInFs
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
        hash_resulting, tempdir = self.prepare_content_to_analyse(expected_content, returnedContent)

        self.assertEqual(expected_content, returnedContent, "Check for results in files hashed as " + hash_resulting + " in " + tempdir)

    def test_getContentWithoutEntryPoint(self):
        self.maxDiff = 10000
    
        contentTemplate = ContentTemplate().setSetupData(getPreparedSetupDateWithoutEntryPoint())
        self.generateSetupContent.setContentTemplate(contentTemplate)
    
        returnedContent = self.generateSetupContent.getContent()
        expected_content = Mocking().getSampleWithoutEntryPoint()
        hash_resulting, tempdir = self.prepare_content_to_analyse(expected_content, returnedContent)

        self.assertEqual(expected_content, returnedContent, "Check for results in files hashed as " + hash_resulting + " in " + tempdir)

    def prepare_content_to_analyse(self, expected, returned):
        now = datetime.datetime.now()
        tempdir = tempfile.gettempdir()
        hash_resulting = savePhysicallyInFs(expected, returned, now, tempdir)
        return hash_resulting, tempdir




