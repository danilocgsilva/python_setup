import re


class SetupData:

    def __init__(self):

        self.requiredData = {
            "name": None,
            "version": "0.0.1",
            "description": None,
            "keywords": None,
            "url": None,
            "author": None,
            "authorEmail": None,
            "package": None
        }

        self.nonRequiredData = {
            "entryPoint": None
        }

    def setName(self, name: str):
        self.requiredData["name"] = name

        if self.requiredData["package"] is None:
            self.requiredData["package"] = self.convertToNamespace(name)

        return self
        
    def getVersion(self) -> str:
        return self.requiredData["version"]

    def getName(self) -> str:
        return self.requiredData["name"]

    def getDescription(self) -> str:
        return self.requiredData["description"]

    def setDescription(self, description: str):
        self.requiredData["description"] = description
        return self

    def getKeywords(self) -> str:
        return self.requiredData["keywords"]

    def setKeywords(self, keywords: str):
        self.requiredData["keywords"] = keywords
        return self

    def getUrl(self) -> str:
        return self.requiredData["url"]

    def setUrl(self, url: str):
        self.requiredData["url"] = url
        return self

    def getAuthor(self) -> str:
        return self.requiredData["author"]

    def setVersion(self, version):
        self.requiredData["version"] = version
        return self

    def setAuthor(self, author: str):
        self.requiredData["author"] = author
        return self

    def getAuthorEmail(self) -> str:
        return self.requiredData["authorEmail"]

    def setAuthorEmail(self, authorEmail: str):
        self.requiredData["authorEmail"] = authorEmail
        return self

    def getPackage(self) -> str:
        package_name = self.requiredData["package"]

        if package_name is None:
            if self.requiredData["name"] is None:
                raise Exception("To get the package name, first you need set the package name or at least set a general name.")
            package_name = self.convertToNamespace(self.requiredData["name"])

        return package_name

    def setPackage(self, package: str):
        self.requiredData["package"] = package
        return self

    def getEntryPoint(self) -> str:
        return self.nonRequiredData["entryPoint"]

    def setEntryPoint(self, entryPoint: str):
        self.nonRequiredData["entryPoint"] = entryPoint
        return self

    def isFullFilled(self) -> bool:
        for key in self.requiredData:
            if self.requiredData[key] is None or self.requiredData[key] == "":
                return False
        return True

    def convertToNamespace(self, original):
        translated = re.sub(r" ", "_", original)
        return translated.lower()
