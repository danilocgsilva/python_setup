from setupPython.SetupData import SetupData
from setupPython.GenerateReadmeContent import GenerateReadmeContent
import os


class Scaffold:

    def __init__(self):
        self.setupData = None

    def setSetupData(self, setupData: SetupData):
        if not setupData.isFullFilled():
            raise Exception("The setup data have missing porperties and we cannot prceed.")
        self.setupData = setupData
        return self

    def generate(self, base_location: str):

        if not os.path.exists(base_location):
            os.makedirs(base_location)

        generateReadmeContent = GenerateReadmeContent()

        readme_file_path = os.path.join(base_location, "README.md")

        self.createFile(readme_file_path, "This is the file content")

    def createFile(self, file_name: str, file_content: str):
        readme_file_resource = open(file_name, "a")
        readme_file_resource.write(file_content + "\n")
        readme_file_resource.close()
