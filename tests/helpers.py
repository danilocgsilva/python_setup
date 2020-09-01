import sys
import os
sys.path.insert(1, "..")
import datetime
import tempfile
from setupPython.SetupData import SetupData
from setupPython.Helpers import Helpers


def getPreparedSetupDate() -> SetupData:

    setupData = SetupData().\
        setVersion("2.2.1").\
        setName("my-app-name").\
        setDescription("This is the description of my application.").\
        setKeywords("those are the keywords").\
        setUrl("http://thisistheversioncontrol.site").\
        setAuthor("Danilo Silva").\
        setAuthorEmail("contact@danilocgsilva.me").\
        setPackage("thepackage").\
        setEntryPoint("executehere")

    return setupData


def getPreparedSetupDateWithoutEntryPoint() -> SetupData:

    setupData = SetupData().\
        setVersion("2.2.1").\
        setName("my-app-name").\
        setDescription("This is the description of my application.").\
        setKeywords("those are the keywords").\
        setUrl("http://thisistheversioncontrol.site").\
        setAuthor("Danilo Silva").\
        setAuthorEmail("contact@danilocgsilva.me").\
        setPackage("thepackage")

    return setupData

def savePhysicallyInFs(returned, expected, datetime, temporary_folder = None):

    if not temporary_folder:
        temporary_folder = tempfile.gettempdir()
    testing_hash = Helpers().getStringTime(datetime)
    os.chdir(temporary_folder)
    open(testing_hash + "-returned", 'a').close()
    open(testing_hash + "-expected", 'a').close()

    return testing_hash

