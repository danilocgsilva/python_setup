import unittest
import sys
sys.path.insert(1, "..")
from setupPython.ContentTemplate import ContentTemplate
from setupPython.SetupData import SetupData
from tests.helpers import getPreparedSetupDate


class test_ContentTemplateInitialData(unittest.TestCase):

    def setUp(self):
        self.contentTemplate = ContentTemplate()

    def test_setSetupDataFluentInterface(self):
        fullfilled_data = getPreparedSetupDate()
        returnedObject = self.contentTemplate.setSetupData(fullfilled_data)
        self.assertTrue(isinstance(returnedObject, ContentTemplate))

    def test_setSetupDataNotFullfilled(self):
        empty_setup_data = SetupData()
        with self.assertRaises(Exception):
            self.contentTemplate.setSetupData(empty_setup_data)

    def test_getVersionTemplate(self):
        expected_string = "VERSION = \"{0}\""
        returned_string = self.contentTemplate.getVersionTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getNameTemplate(self):
        expected_string = "    name=\"{0}\","
        returned_string = self.contentTemplate.getNameTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getDescriptionTemplate(self):
        expected_string = "    description=\"{0}\","
        returned_string = self.contentTemplate.getDescriptionTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getKeywordsTemplate(self):
        expected_string = "    keywords=\"{0}\","
        returned_string = self.contentTemplate.getKeywordsTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getAuthorTemplate(self):
        expected_string = "    author=\"{0}\","
        returned_string = self.contentTemplate.getAuthorTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getAuthorEmailTemplate(self):
        expected_string = "    author_email=\"{0}\","
        returned_string = self.contentTemplate.getAuthorEmailTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getPackageTemplate(self):
        expected_string = "    packages=[\"{0}\"],"
        returned_string = self.contentTemplate.getPackageTemplate()
        self.assertEqual(expected_string, returned_string)

    def test_getPackageEntryPoints(self):
        expected_string = "[\"{0}={1}.__main__:main\"],"
        returned_string = self.contentTemplate.getEntryPoints()

        self.assertEqual(expected_string, returned_string)
