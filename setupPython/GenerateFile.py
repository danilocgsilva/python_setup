import pkg_resources
from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate


class GenerateFile:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"
        self.contentTemplate = ContentTemplate

    def setSetupData(self, setupData: SetupData):
        self.setupData = setupData
        return self

    def generate(self) -> str:
        valuedContentTemplate = ""
        valuedContentTemplate += self.set

        return valuedContentTemplate
