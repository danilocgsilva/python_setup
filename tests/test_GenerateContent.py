import unittest
import sys
import tempfile
sys.path.insert(1, "..")
from setupPython.GenerateContent import GenerateContent
from setupPython.SetupData import SetupData


class test_GenerateContent(unittest.TestCase):

    def setUp(self):
        self.generateContent = GenerateContent()
        self.setupData = SetupData()
    
    def test_generateFileWithCorrectData(self):

        utilityName = "MyUtilityTest"
        description = "This is the description of the script."
        keywords = "this is the keywords"
        url = "https://url/from/project"
        author = "Danilo Silva"
        authorEmail = "contato@danilocgsilva.me"
        entryPoints = "executeme"

        self.setupData.\
            setName(utilityName).\
            setDescription(description).\
            setKeyword(keywords).\
            setUrl(url).\
            setAuthor(author).\
            setAuthorEmail(authorEmail).\
            setEntryPoint(entryPoints)

        self.generateFile.setSetupData(self.setupData)
        self.generateFile.generate()
