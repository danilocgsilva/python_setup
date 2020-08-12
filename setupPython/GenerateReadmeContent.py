class GenerateReadmeContent:

    def __init__(self):
        self.title = None

    def setTitle(self, title: str):
        self.title = title
        return self

    def getContent(self) -> str:
        content = "# " + self.title + "\n"
        content += "\n"
        content += "Give some human readable data here.\n"

        return content
