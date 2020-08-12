import re


class ContentTemplate:

    def __init__(self):
        self.contentList = self.getInitialContentTemplateList()
        self.TEMPLATE_VERSION_POSITION = 2
        self.TEMPLATE_NAME_POSITON = 9
        self.TEMPLATE_DESCRIPTION_POSITON = 11
        self.TEMPLATE_KEYWORDS_POSITON = 14
        self.TEMPLATE_URL_POSITON = 15
        self.TEMPLATE_AUTHOR_POSITION = 16
        self.TEMPLATE_AUTHOREMAIL_POSITION = 17
        self.TEMPLATE_PACKAGE_POSITION = 18
        self.TEMPLATE_ENTRYPOINTS_POSITION = 20

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

        contentList = self.contentList[self.TEMPLATE_PACKAGE_POSITION]

        if re.search('{"', contentList):
            splittingCharacter = '{'
            splittingCharacterOposite = '}'
        else:
            splittingCharacter = '"'
            splittingCharacterOposite = '"'

        return contentList.split(splittingCharacter)[1].split(splittingCharacterOposite)[0]

    def getInitialContentTemplateList(self) -> list:

        contentList = []

        contentList.append("from setuptools import setup")
        contentList.append("")
        contentList.append("VERSION = {0}")
        contentList.append("")
        contentList.append("def readme():")
        contentList.append("    with open(\"README.md\") as f:")
        contentList.append("        return f.read()")
        contentList.append("")
        contentList.append("setup(")
        contentList.append("    name=\"{0}\",")
        contentList.append("    version=VERSION,")
        contentList.append("    description=\"{0}\",")
        contentList.append("    long_description_content_type=\"text/markdown\",")
        contentList.append("    long_description=readme(),")
        contentList.append("    keywords=\"{0}\",")
        contentList.append("    url=\"{0}\",")
        contentList.append("    author=\"{0}\",")
        contentList.append("    author_email=\"{0}\",")
        contentList.append("    packages=[\"{0}\"],")
        contentList.append("    entry_points={\"console_scripts\": )")
        contentList.append("[\"{0}={1}.__main__:main\"],")
        contentList.append("},")
        contentList.append("    include_package_data=True")
        contentList.append(")")

        return contentList
