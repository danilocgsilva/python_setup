import unittest
import sys
sys.path.insert(1, "..")
from setupPython.SetupData import SetupData
from tests.helpers import getPreparedSetupDate

class test_SetupData(unittest.TestCase):

    def setUp(self):
        self.setupData = SetupData()

    def test_getVersion(self):
        defaultVersion = "0.0.1"
        returnedVersion = self.setupData.getVersion()
        self.assertEqual(defaultVersion, returnedVersion)

    def test_setNameFluentInterface(self):
        returnedObject = self.setupData.setName("any-name")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setDescriptionFluentInterface(self):
        returnedObject = self.setupData.setDescription("Some description")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setKeywordsFluentInterface(self):
        returnedObject = self.setupData.setKeywords("Some Words")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setUrlFluentInterface(self):
        returnedObject = self.setupData.setUrl("http://any.com")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setAuthorEmailFluentInterface(self):
        returnedObject = self.setupData.setAuthorEmail("contato@danilocgsilva.me")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setAuthorFluentInterface(self):
        returnedObject = self.setupData.setAuthor("Danilo Silva")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setPackageFluentInterface(self):
        returnedObject = self.setupData.setPackage("scriptpackage")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setEntryPointFluentInterface(self):
        returnedObject = self.setupData.setEntryPoint("executehere")
        self.assertTrue(isinstance(returnedObject, SetupData))

    def test_setVersionFluentInterface(self):
        returnendObject = self.setupData.setVersion("3.2.1")
        self.assertTrue(isinstance(returnendObject, SetupData))

    def test_isFullFilledFalse(self):
        self.assertFalse(self.setupData.isFullFilled())

    def test_isFullFilledTrue(self):
        setupDataFullFilled = getPreparedSetupDate()
        self.assertTrue(setupDataFullFilled.isFullFilled())

    def test_isFullFilledFalseWithStringsSingle(self):
        setupData = SetupData(). \
            setVersion("2.2.1"). \
            setName("my-app-name"). \
            setDescription(""). \
            setKeywords("those are the keywords"). \
            setUrl("http://thisistheversioncontrol.site"). \
            setAuthor("Danilo Silva"). \
            setAuthorEmail("contact@danilocgsilva.me"). \
            setPackage("thepackage"). \
            setEntryPoint("executehere")

        self.assertFalse(setupData.isFullFilled())

    def test_isFullFilledFalseForget(self):
        setupData = SetupData(). \
            setVersion("2.2.1"). \
            setName("my-app-name"). \
            setDescription(""). \
            setUrl("http://thisistheversioncontrol.site"). \
            setAuthor("Danilo Silva"). \
            setAuthorEmail("contact@danilocgsilva.me"). \
            setPackage("thepackage"). \
            setEntryPoint("executehere")

        self.assertFalse(setupData.isFullFilled())

    def test_getPackageDefaultPackageWithoutName(self):
        with self.assertRaises(Exception):
            self.setupData.getPackage()

    def test_getPackageDefaultWithName(self):
        self.setupData.setName("My Package Name")
        expected_package_name = "my_package_name"
        package_name_returned = self.setupData.getPackage()
        self.assertEqual(expected_package_name, package_name_returned)

    def test_convertToNamespace(self):
        original_term = "This is my App"
        expected_result = "this_is_my_app"
        returned_result = self.setupData.convertToNamespace(original_term)
        self.assertEqual(expected_result, returned_result)

    def test_isFullFilledWithoutPackage(self):
        setupData = SetupData().\
            setVersion("2.2.1").\
            setName("my-app-name").\
            setDescription("This is the description of my application.").\
            setKeywords("those are the keywords").\
            setUrl("http://thisistheversioncontrol.site").\
            setAuthor("Danilo Silva").\
            setAuthorEmail("contact@danilocgsilva.me").\
            setEntryPoint("executehere")
        self.assertTrue(setupData.isFullFilled())
