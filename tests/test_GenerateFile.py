import unittest
import tempfile
import os
import sys
sys.path.insert(1, "..")
from setupPython.GenerateFile import GenerateFile
from setupPython.ContentTemplate import ContentTemplate
from setupPython.SetupData import SetupData
from tests.helpers import getPreparedSetupDate

class test_GenerateFile(unittest.TestCase):

    def setUp(self):
        self.generateFile = GenerateFile()

    def test_setContentTemplateFluentInterface(self):
        contentTemplate = ContentTemplate()
        returnedObject = self.generateFile.setContentTemplate(contentTemplate)
        self.assertTrue(isinstance(returnedObject, GenerateFile))

    def test_writeFileCorrectContent(self):
        self.maxDiff = 10000

        contentTemplate = ContentTemplate()
        contentTemplate.setSetupData(getPreparedSetupDate())
        self.generateFile.setContentTemplate(contentTemplate)

        temporaryFilePath = os.path.join(tempfile.gettempdir(), "setupTest.py")

        if os.path.exists(temporaryFilePath):
            os.remove(temporaryFilePath)

        self.generateFile.writeFile(temporaryFilePath)

        fileToFetch = open(temporaryFilePath, "r")
        fetchedContent = fileToFetch.read()

        fileToFetch.close()

        expected_content = '''from setuptools import setup

VERSION = 2.2.1

def readme():
    with open(\"README.md\") as f:
        return f.read()

setup(
    name="my-app-name",
    version=VERSION,
    description="This is the description of my application.",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="those are the keywords",
    url="http://thisistheversioncontrol.site",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["thepackage"],
    entry_points={"console_scripts": ["executehere=thepackage.__main__:main"],},
    include_package_data=True
)
'''

        self.assertEqual(expected_content, fetchedContent)

