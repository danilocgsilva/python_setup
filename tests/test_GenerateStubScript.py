import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateStubScript import GenerateStubScript


class test_GenerateStubScript(unittest.TestCase):

    def setUp(self) -> None:
        self.generateStubScript = GenerateStubScript()

    def test_generateDefaultContent(self):

        app_name = "Beautiful Script"

        expected_content = "def main():" + "\n"
        expected_content += '    print("Hello World! Starts here the Beautiful Script program to change the world!")' + "\n"

        self.generateStubScript.setTitle(app_name)
        returned_content = self.generateStubScript.getContent()

        self.assertEqual(expected_content, returned_content)

    def test_triesGenerateStubContentWithoutNameSetted(self):
        with self.assertRaises(Exception):
            self.generateStubScript.getContent()

    def test_setTitleFluentInterface(self):
        returned_object = self.generateStubScript.setTitle("Some App Title")
        self.assertTrue(isinstance(returned_object, GenerateStubScript))
