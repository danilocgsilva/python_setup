import pkg_resources
from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate


class GenerateFile:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"
        self.contentTemplate = None

    def setSetupData(self, setupData: SetupData):
        self.setupData = setupData
        return self

    def setContentTemplate(self, contentTemplate: ContentTemplate):
        self.contentTemplate = contentTemplate
        return self

    def generate(self) -> str:
        valuedContentTemplate = ""

        return valuedContentTemplate
