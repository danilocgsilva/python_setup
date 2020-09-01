import unittest
import sys
import datetime
import tempfile
import os
sys.path.insert(1, "..")
from tests.helpers import savePhysicallyInFs
from setupPython.Helpers import Helpers


class test_Helpers(unittest.TestCase):

    def setUp(self):
        self.helpers = Helpers()

    def test_getStringTime(self):
        string_expected = "20190806_09h08m01s-546434"
        datetime_custom_date = datetime.datetime.strptime("06.08.2019 09:08:01,546434", "%d.%m.%Y %H:%M:%S,%f")
        returned_string = self.helpers.getStringTime(datetime_custom_date)
        self.assertEqual(string_expected, returned_string)

    def test_savePhysicallyInFs(self):
        string_expected = "20190806_09h08m01s-546434"
        datetime_custom_date = datetime.datetime.strptime("06.08.2019 09:08:01,546434", "%d.%m.%Y %H:%M:%S,%f")
        hash = savePhysicallyInFs("a", "a", datetime_custom_date)
        self.assertEqual(string_expected, hash)

    def test_savePhysicallyInFsFileCreation(self):
        temporary_test_directory = os.path.join(tempfile.gettempdir(), 'python_setup_temp_dir')
        if not os.path.exists(temporary_test_directory):
            os.makedirs(temporary_test_directory)
        os.chdir(temporary_test_directory)

        for file in os.listdir():
            os.remove(file)
    
        datetime_custom_date = datetime.datetime.strptime("06.08.2019 09:08:01,546434", "%d.%m.%Y %H:%M:%S,%f")
        savePhysicallyInFs("a", "a", datetime_custom_date, temporary_test_directory)
        expected_file_list = ["20190806_09h08m01s-546434-expected", "20190806_09h08m01s-546434-returned"]
        self.assertListEqual(expected_file_list, os.listdir())
