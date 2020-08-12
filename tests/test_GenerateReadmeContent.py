import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateReadmeContent import GenerateReadmeContent


class test_GenerateReadmeContent(unittest.TestCase):

    def setUp(self) -> None:
        self.generateReadmeContent = GenerateReadmeContent()

    def test_getContentWithoutTitle(self):
        with self.assertRaises(Exception):
            self.generateReadmeContent.getContent()

    def test_getContent(self):

        title = "my_project"
        self.generateReadmeContent.setTitle(title)

        expected_content = '''# my_project

Give some human readable data here.
'''

        returnedContent = self.generateReadmeContent.getContent()

        self.assertEqual(expected_content, returnedContent)

    def test_getContent2(self):

        title = "Another Title"
        self.generateReadmeContent.setTitle(title)

        expected_content = '''# Another Title

Give some human readable data here.
'''

        returnedContent = self.generateReadmeContent.getContent()

        self.assertEqual(expected_content, returnedContent)
