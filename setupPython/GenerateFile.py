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

    def writeFile(self, filePath: str):
        file = open(filePath, "a")
        contentList = self.contentTemplate.getContentTemplateList()

        for i in range(0, 19):
            file.write(contentList[i])

        for i in range(20, 22):
            file.write(contentList[i])

        for i in range(23, len(contentList)):
            file.write(contentList[i])

        file.close()
