from setupPython.SetupData import SetupData
from setupPython.GenerateReadmeContent import GenerateReadmeContent
import os


class Scaffold:

    def __init__(self):
        self.setupData = None
        self.package = None
        self.basePath = None
        self.fileDict = {}

    def setBasePath(self, base_path: str):
        self.basePath = base_path
        return self

    def setSetupContent(self, content: str):
        self.fileDict["setup.py"] = content
        return self

    def setReadmeContent(self, content: str):
        self.fileDict["README.md"] = content
        return self

    def setPackage(self, package: str):
        self.package = package
        return self

    def setMainContent(self, content: str):
        self.fileDict[os.path.join(self.package, "__main__.py")] = content
        return self

    def setSetupData(self, setupData: SetupData):
        if not setupData.isFullFilled():
            raise Exception("The setup data have missing properties and we cannot proceed.")
        self.setupData = setupData
        return self

    def generate(self, base_location: str):

        if not os.path.exists(base_location):
            os.makedirs(base_location)

        for file_key in self.fileDict:
            self.createFile(file_key, self.fileDict[file_key])

    def createFile(self, file_name: str, file_content: str):

        if self.basePath == None:
            raise Exception("You need to set the base path first.")

        if not os.path.exists(self.basePath):
            os.makedirs(self.basePath)

        file_resource = open(os.path.join(self.basePath, file_name), "a")
        print(os.path.join(self.basePath, file_name))
        file_resource.write(file_content + "\n")
        file_resource.close()
