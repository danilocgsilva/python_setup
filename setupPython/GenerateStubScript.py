class GenerateStubScript:

    def __init__(self):
        self.title = None

    def setTitle(self, title: str):
        self.title = title
        return self

    def getContent(self):
        content = "def main():" + "\n"
        content += '    print("Hello World! Starts here the ' + self.title + ' program to change the world!")' + "\n"

        return content
