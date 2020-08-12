import sys
sys.path.insert(1, "..")
from setupPython.SetupData import SetupData

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
