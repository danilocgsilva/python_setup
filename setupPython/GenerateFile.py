from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate


class GenerateFile:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"
        self.contentTemplate = None

    def setContentTemplate(self, contentTemplate: ContentTemplate):
        self.contentTemplate = contentTemplate
        return self

    def getSetupContent(self):

        setupContent = ""

        contentList = self.contentTemplate.getContentTemplateList()

        for i in range(0, 19):
            setupContent += contentList[i] + "\n"
        for i in range(19, 21):
            setupContent += contentList[i]
        for i in range(21, len(contentList)):
            setupContent += contentList[i] + "\n"

        return setupContent
