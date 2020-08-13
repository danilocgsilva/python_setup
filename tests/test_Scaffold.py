import unittest
import tempfile
import os
import sys
sys.path.insert(1, "..")
from setupPython.Scaffold import Scaffold
from setupPython.SetupData import SetupData
from tests.helpers import getPreparedSetupDate


class test_Scaffold(unittest.TestCase):

    def setUp(self) -> None:
        self.scaffold = Scaffold()

    def test_triesAssingNotFullfilledSetupData(self):
        setupData = SetupData()
        with self.assertRaises(Exception):
            self.scaffold.setSetupData(setupData)

    def test_setSetupDataFluentInterface(self):
        setupDataFullfilled = getPreparedSetupDate()
        returnedObject = self.scaffold.setSetupData(setupDataFullfilled)
        self.assertTrue(isinstance(returnedObject, Scaffold))

    def test_generate(self):
        base_location = os.path.join(tempfile.gettempdir(), 'scaffold_test')
        self.scaffold.generate(base_location)
        os.chdir(base_location)
        self.assertTrue(os.path.exists("README.md"))

    def test_setSetupContentFluentInterface(self):
        stub_content = "This is stub content"
        returned_object = self.scaffold.setSetupContent(stub_content)
        self.assertTrue(isinstance(returned_object, Scaffold))

    def test_setReadmeContentFluentInterface(self):
        stub_content = "This is stub content for readme"
        returned_object = self.scaffold.setReadmeContent(stub_content)
        self.assertTrue(isinstance(returned_object, Scaffold))

    def test_setPackageFluentInterface(self):
        stub_content = "scriptpackage"
        returned_object = self.scaffold.setPackage(stub_content)
        self.assertTrue(isinstance(returned_object, Scaffold))

    def test_setMainContentForgettingPackage(self):
        stub_content = "def() the main content"
        with self.assertRaises(Exception):
            self.scaffold.setMainContent(stub_content)

    def test_setMainContentFluentInterface(self):
        stub_content = "def() the main content"
        stup_package = "scriptpackage"

        returned_object = self.scaffold\
            .setPackage(stup_package)\
            .setMainContent(stub_content)
        
        self.assertTrue(isinstance(returned_object, Scaffold))
