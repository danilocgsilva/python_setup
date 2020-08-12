import unittest
import sys
sys.path.insert(1, "..")
from tests.helpers import getPreparedSetupDate
from setupPython.ContentTemplate import ContentTemplate
from setupPython.SetupData import SetupData


class test_ContentTemplateInitialData(unittest.TestCase):

    def setUp(self):
        self.contentTemplate = ContentTemplate()
        self.setupData = getPreparedSetupDate()
        self.contentTemplate.setSetupData(self.setupData)

    def test_setVersion(self):
        expected_template = "VERSION = 2.2.1"
        resulting_template = self.contentTemplate.getVersionTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setName(self):
        expected_template = "    name=\"my-app-name\","
        resulting_template = self.contentTemplate.getNameTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setDescription(self):
        expected_template = "    description=\"This is the description of my application.\","
        resulting_template = self.contentTemplate.getDescriptionTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setKeywords(self):
        expected_template = "    keywords=\"those are the keywords\","
        resulting_template = self.contentTemplate.getKeywordsTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setUrl(self):
        expected_template = "    url=\"http://thisistheversioncontrol.site\","
        resulting_template = self.contentTemplate.getUrlTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setAuthor(self):
        expected_template = "    author=\"Danilo Silva\","
        resulting_template = self.contentTemplate.getAuthorTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setAuthorEmail(self):
        expected_template = "    author_email=\"contact@danilocgsilva.me\","
        resulting_template = self.contentTemplate.getAuthorEmailTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setPackage(self):
        expected_template = "    packages=[\"thepackage\"],"
        resulting_template = self.contentTemplate.getPackageTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_exceptionSetEntryPoints(self):
        entry_point = "executehere"
        with self.assertRaises(Exception):
            self.contentTemplate.setEntryPoint(entry_point)

    def test_setEntryPoint(self):
        package = "thepackage"
        entry_point = "executehere"

        expected_template = "[\"executehere=thepackage.__main__:main\"],"
        resulting_template = self.contentTemplate.getEntryPoints()
        self.assertEqual(expected_template, resulting_template)
