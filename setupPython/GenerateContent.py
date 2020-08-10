from setupPython.SetupData import SetupData


class GenerateContent:

    def __init__(self):
        self.setupData = None
        self.fileName = "setup.py"

    def setSetupData(self, setupData: SetupData):
        self.setSetupData - setupData
        return self

    def generate(self):
        file = open(self.fileName)
        file.write()
        file.close()
