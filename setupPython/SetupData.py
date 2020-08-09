class SetupData:

    def __init__(self):
        self.name = None
        self.version = "0.0.1"
        self.description = None
        self.keywords = None
        self.url = None
        self.author = None
        self.authorEmail = None
        self.entryPoint = None
    
    def setName(self, name: str):
        self.name = name
        return self

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description: str):
        self.description = description
        return self

    def getKeywords(self) -> str:
        return self.keywords

    def setKeywords(self, keywords: str):
        self.keywords = keywords
        return self

    def getUrl(self) -> str:
        return self.url

    def setUrl(self, url: str):
        self.url = url
        return self

    def getAuthor(self) -> str:
        return self.author

    def setAuthor(self, author: str):
        self.author = author
        return self

    def getAuthorEmail(self) -> str:
        return self.authorEmail

    def setAuthorEmail(self, authorEmail: str):
        self.authorEmail = authorEmail
        return self

    def getEntryPoint(self) -> str:
        return self.entryPoint

    def setEntryPoint(self, entryPoint: str):
        self.entryPoint = entryPoint
        return self

