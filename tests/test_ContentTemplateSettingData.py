import unittest
import sys
sys.path.insert(1, "..")
from setupPython.ContentTemplate import ContentTemplate
from setupPython.SetupData import SetupData


class test_ContentTemplateInitialData(unittest.TestCase):

    def setUp(self):
        self.contentTemplate = ContentTemplate()
        self.setupData = SetupData().\
            setVersion("2.2.1").\
            setName("my-app-name").\
            setDescription("This is the description of my application.").\
            setKeywords("those are the keywords").\
            setUrl("http://thisistheversioncontrol.site").\
            setAuthor("Danilo Silva").\
            setAuthorEmail("contact@danilocgsilva.me")


    def test_setVersion(self):
        version = "2.2.1"
        expected_template = "VERSION = 2.2.1"
        self.contentTemplate.setVersion(version)
        resulting_template = self.contentTemplate.getVersionTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setName(self):
        name = "my-app-name"
        expected_template = "    name=\"my-app-name\","
        self.contentTemplate.setName(name)
        resulting_template = self.contentTemplate.getNameTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setDescription(self):
        description = "This is the description of my application."
        expected_template = "    description=\"This is the description of my application.\","
        self.contentTemplate.setDescription(description)
        resulting_template = self.contentTemplate.getDescriptionTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setKeywords(self):
        keywords = "those are the keywords"
        expected_template = "    keywords=\"those are the keywords\","
        self.contentTemplate.setKeywords(keywords)
        resulting_template = self.contentTemplate.getKeywordsTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setUrl(self):
        url = "http://thisistheversioncontrol.site"
        expected_template = "    url=\"http://thisistheversioncontrol.site\","
        self.contentTemplate.setUrl(url)
        resulting_template = self.contentTemplate.getUrlTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setAuthor(self):
        author = "Danilo Silva"
        expected_template = "    author=\"Danilo Silva\","
        self.contentTemplate.setAuthor(author)
        resulting_template = self.contentTemplate.getAuthorTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setAuthorEmail(self):
        authorEmail = "contact@danilocgsilva.me"
        expected_template = "    author_email=\"contact@danilocgsilva.me\","
        self.contentTemplate.setAuthorEmail(authorEmail)
        resulting_template = self.contentTemplate.getAuthorEmailTemplate()
        self.assertEqual(expected_template, resulting_template)

    def test_setPackage(self):
        package = "thepackage"
        expected_template = "    packages=[\"thepackage\"],"
        self.contentTemplate.setPackage(package)
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
        self.contentTemplate.setPackage(package)
        self.contentTemplate.setEntryPoint(entry_point)
        resulting_template = self.contentTemplate.getEntryPoints()
        self.assertEqual(expected_template, resulting_template)
