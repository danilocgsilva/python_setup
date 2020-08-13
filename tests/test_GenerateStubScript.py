import unittest
import sys
sys.path.insert(1, "..")
from setupPython.GenerateStubScript import GenerateStubScript


class test_GenerateStubScript(unittest.TestCase):

    def setUp(self) -> None:
        self.generateStubScript = GenerateStubScript()

    def test_generateDefaultContent(self):
        expected_content = "def main():" + "\n"
        expected_content += '    print("Hello World! Starts here your script to change the world!")' + "\n"

        returned_content = self.generateStubScript.getContent()

        self.assertEqual(expected_content, returned_content)
