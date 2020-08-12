import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.ContentTemplate import ContentTemplate
from tests.helpers import getPreparedSetupDate

class test_GenerateSetupContent(unittest.TestCase):

    def setUp(self):
        self.generateSetupContent = GenerateSetupContent()

    def test_setContentTemplateFluentInterface(self):
        contentTemplate = ContentTemplate()
        returnedObject = self.generateSetupContent.setContentTemplate(contentTemplate)
        self.assertTrue(isinstance(returnedObject, GenerateSetupContent))

    def test_getSetupContent(self):
        self.maxDiff = 10000

        contentTemplate = ContentTemplate()
        contentTemplate.setSetupData(getPreparedSetupDate())
        self.generateSetupContent.setContentTemplate(contentTemplate)

        returnedContent = self.generateSetupContent.getSetupContent()

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

        self.assertEqual(expected_content, returnedContent)

