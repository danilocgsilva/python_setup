from setupPython.SetupData import SetupData


class GenerateFile:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"

    def setSetupData(self, setupData: SetupData):
        self.setSetupData - setupData
        return self

    def generateFile(self):
        file = open(self.fileName)
        file.close()
