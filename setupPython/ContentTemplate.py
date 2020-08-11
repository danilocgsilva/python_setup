from setupPython.helpers import getContentTemplateList


class ContentTemplate:

    def __init__(self):
        self.contentList = getContentTemplateList()
        self.TEMPLATE_VERSION_POSITION = 2
        self.TEMPLATE_NAME_POSITON = 9
        self.TEMPLATE_DESCRIPTION_POSITON = 11
        self.TEMPLATE_KEYWORDS_POSITON = 14
        self.TEMPLATE_URL_POSITON = 15
        self.TEMPLATE_AUTHOR_POSITION = 16
        self.TEMPLATE_AUTHOREMAIL_POSITION = 17
        self.TEMPLATE_PACKAGE_POSITION = 18
        self.TEMPLATE_ENTRYPOINTS_POSITION = 19

    def getContentTemplateList(self) -> list:
        return self.contentList

    def getVersionTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_VERSION_POSITION]

    def getNameTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_NAME_POSITON]

    def getDescriptionTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_DESCRIPTION_POSITON]

    def getKeywordsTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_KEYWORDS_POSITON]

    def getUrlTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_URL_POSITON]

    def getAuthorTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_AUTHOR_POSITION]

    def getAuthorEmailTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_AUTHOREMAIL_POSITION]

    def getPackageTemplate(self) -> str:
        return self.contentList[self.TEMPLATE_PACKAGE_POSITION]

    def getEntryPoints(self) -> str:
        return self.contentList[self.TEMPLATE_ENTRYPOINTS_POSITION]

    def getPackageValue(self) -> str:
        return self.contentList[self.TEMPLATE_PACKAGE_POSITION].split("{")[1].split("}")[0]

    def setVersion(self, version: str):
        versionTemplate = self.getVersionTemplate()
        self.contentList[self.TEMPLATE_VERSION_POSITION] = versionTemplate.format(version)
        return self

    def setName(self, name: str):
        nameTemplate = self.getNameTemplate()
        self.contentList[self.TEMPLATE_NAME_POSITON] = nameTemplate.format(name)
        return self

    def setDescription(self, description: str):
        descriptionTemplate = self.getDescriptionTemplate()
        self.contentList[self.TEMPLATE_DESCRIPTION_POSITON] = descriptionTemplate.format(description)
        return self

    def setKeywords(self, keywords: str):
        keywordsTemplate = self.getKeywordsTemplate()
        self.contentList[self.TEMPLATE_KEYWORDS_POSITON] = keywordsTemplate.format(keywords)
        return self

    def setUrl(self, url: str):
        urlTemplate = self.getUrlTemplate()
        self.contentList[self.TEMPLATE_URL_POSITON] = urlTemplate.format(url)
        return self

    def setAuthor(self, author: str):
        authorTemplate = self.getAuthorTemplate()
        self.contentList[self.TEMPLATE_AUTHOR_POSITION] = authorTemplate.format(author)
        return self

    def setAuthorEmail(self, authorEmail: str):
        authorEmailTemplate = self.getAuthorEmailTemplate()
        self.contentList[self.TEMPLATE_AUTHOREMAIL_POSITION] = authorEmailTemplate.format(authorEmail)
        return self

    def setPackage(self, package: str):
        packageTemplate = self.getPackageTemplate()
        self.contentList[self.TEMPLATE_PACKAGE_POSITION] = packageTemplate.format(package)
        return self

    def setEntryPoint(self, entryPoint: str):
        entryPointTemplate = self.getEntryPoints()
        if entryPointTemplate == "    packages=[\"{0}\"],":
            raise Exception("The setPackageEntryPoints cannot be performed if you do not set the package template first with setPackageTemplate method")
        self.contentList[self.TEMPLATE_ENTRYPOINTS_POSITION] = entryPointTemplate.format(entryPoint, self.getPackageValue())
        return self
