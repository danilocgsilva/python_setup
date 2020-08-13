import re


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

        if self.data["package"] is None:
            self.data["package"] = self.convertToNamespace(name)

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
        package_name = self.data["package"]

        if package_name is None:
            if self.data["name"] is None:
                raise Exception("To get the package name, first you need set the package name or at least set a general name.")
            package_name = self.convertToNamespace(self.data["name"])

        return package_name

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

    def convertToNamespace(self, original):
        translated = re.sub(r" ", "_", original)
        return translated.lower()
