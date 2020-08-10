import pkg_resources
from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate


class GenerateContent:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"
        self.contentTemplate = ContentTemplate

    def setSetupData(self, setupData: SetupData):
        self.setupData = setupData
        return self

    def generate(self) -> str:
        contentTemplate = ContentTemplate().getContentTemplateList()

        version = self.setupData.getVersion()
        name = self.setupData.getName()
        description = self.setupData.getDescription()
        keywords = self.setupData.getKeywords()
        url = self.setupData.getUrl()
        author = self.setupData.getAuthor()
        email = self.setupData.getAuthorEmail()
        package = self.setupData.getPackage()
        entryPoint = self.setupData.getEntryPoint()

        valuedContentTemplate =  contentTemplate.format(
            version,
            name,
            description,
            keywords,
            url,
            author,
            email,
            package,
            entryPoint
        )

        return valuedContentTemplate
