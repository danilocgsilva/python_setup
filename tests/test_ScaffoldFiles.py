import unittest
import sys
import os
import tempfile
import shutil
sys.path.insert(1, "..")
from setupPython.Scaffold import Scaffold


class test_ScaffoldFiles(unittest.TestCase):

    def setUp(self) -> None:
        self.scaffold = Scaffold()
        self.tests_base_location_files = os.path.join(tempfile.gettempdir(), 'scaffold_test')
        if os.path.exists(self.tests_base_location_files):
            shutil.rmtree(self.tests_base_location_files)
        self.scaffold = Scaffold().setBasePath(self.tests_base_location_files)

    def test_generateReadmeExists(self):
        self.scaffold.setReadmeContent("This is the readme content!")
        self.scaffold.generate()

        os.chdir(self.tests_base_location_files)
        self.assertTrue(os.path.exists("README.md"))

    def test_generateSetupExists(self):
        self.scaffold.setSetupContent("Another content")
        self.scaffold.generate()

        os.chdir(self.tests_base_location_files)
        self.assertTrue(os.path.exists("setup.py"))

    def test_generateMainWithoutPackage(self):
        with self.assertRaises(Exception):
            self.scaffold.setMainContent("def main content")

    def test_generateMain(self):
        self.scaffold.setPackage("apppackage")
        self.scaffold.setMainContent("def main content")
        self.scaffold.generate()

        os.chdir(self.tests_base_location_files)
        self.assertTrue(os.path.exists(os.path.join("apppackage", "__main__.py")))

    def test_createFileFileContent(self):
        some_file_title = "hello.txt"
        some_file_content = "Hi! I exists!"
        self.scaffold.setBasePath(self.tests_base_location_files)
        self.scaffold.createFile(some_file_title, some_file_content)

        just_create_file_path = os.path.join(self.tests_base_location_files, some_file_title)
        just_create_file_resource = open(just_create_file_path)
        just_create_file_content = just_create_file_resource.read()
        just_create_file_resource.close()

        self.assertEqual(some_file_content + "\n", just_create_file_content)

    def test_createFileReturnString(self):
        some_file_title = "hello.js"
        some_file_content = "Hi! I exists!"
        self.scaffold.setBasePath(self.tests_base_location_files)
        file_to_create = self.scaffold.createFile(some_file_title, some_file_content)
        self.assertEqual(some_file_title, file_to_create)

    def test_createFileReturnStringOneLevel(self):
        some_file_title = "package" + os.sep + "hello.js"
        some_file_content = "Hi! I exists!"
        self.scaffold.setBasePath(self.tests_base_location_files)
        file_to_create = self.scaffold.createFile(some_file_title, some_file_content)
        self.assertEqual(some_file_title, file_to_create)


    def getFileContent(self, file_path: str):
        readme_resource = open(file_path)
        file_content = readme_resource.read()
        readme_resource.close()
        return file_content
