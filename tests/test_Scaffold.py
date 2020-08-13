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

    def test_setSetupContent(self):
        self.assertTrue(False)

    def test_setReadmeContent(self):
        self.assertTrue(False)

    def test_setPackage(self):
        self.assertTrue(False)

    def test_setMainContent(self):
        self.assertTrue(False)
