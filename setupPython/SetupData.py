class SetupData:

    def __init__(self):

        self.data = {
            "name": None,
            "version": "0.0.1",
            "description": None,
            "keywords": None,
            "url": None,
            "author": None,
            "authorEmail": None,
            "package": None,
            "entryPoint": None
        }

    def setName(self, name: str):
        self.data["name"] = name
        return self
        
    def getVersion(self) -> str:
        return self.data["version"]

    def getName(self) -> str:
        return self.data["name"]

    def getDescription(self) -> str:
        return self.data["description"]

    def setDescription(self, description: str):
        self.data["description"] = description
        return self

    def getKeywords(self) -> str:
        return self.data["keywords"]

    def setKeywords(self, keywords: str):
        self.data["keywords"] = keywords
        return self

    def getUrl(self) -> str:
        return self.data["url"]

    def setUrl(self, url: str):
        self.data["url"] = url
        return self

    def getAuthor(self) -> str:
        return self.data["author"]

    def setVersion(self, version):
        self.data["version"] = version
        return self

    def setAuthor(self, author: str):
        self.data["author"] = author
        return self

    def getAuthorEmail(self) -> str:
        return self.data["authorEmail"]

    def setAuthorEmail(self, authorEmail: str):
        self.data["authorEmail"] = authorEmail
        return self

    def getPackage(self) -> str:
        return self.data["package"]

    def setPackage(self, package: str):
        self.data["package"] = package
        return self

    def getEntryPoint(self) -> str:
        return self.data["entryPoint"]

    def setEntryPoint(self, entryPoint: str):
        self.data["entryPoint"] = entryPoint
        return self

    def isFullFilled(self) -> bool:
        for key in self.data:
            if self.data[key] is None or self.data[key] == "":
                return False
        return True
