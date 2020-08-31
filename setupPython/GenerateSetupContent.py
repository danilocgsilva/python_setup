from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate


class GenerateSetupContent:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"
        self.contentTemplate = None

    def setContentTemplate(self, contentTemplate: ContentTemplate):
        self.contentTemplate = contentTemplate
        return self

    def getContent(self):

        setupContent = ""

        contentList = self.contentTemplate.getContentTemplateList()

        for i in range(0, len(contentList)):
            setupContent += contentList[i] + "\n"

        return setupContent
