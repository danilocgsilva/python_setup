import re
from setupPython.SetupData import SetupData


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
        self.setupData = None

    def setSetupData(self, setupData: SetupData):

        if not setupData.isFullFilled():
            raise Exception("There are missing informations in the setupData object.")

        forged_list = []

        self.setupData = setupData

        forged_list.append(self.contentList[0])
        forged_list.append(self.contentList[1])
        forged_list.append(self.contentList[self.TEMPLATE_VERSION_POSITION].format(self.setupData.getVersion()))
        forged_list.append(self.contentList[3])
        forged_list.append(self.contentList[4])
        forged_list.append(self.contentList[5])
        forged_list.append(self.contentList[6])
        forged_list.append(self.contentList[7])
        forged_list.append(self.contentList[8])
        forged_list.append(self.contentList[self.TEMPLATE_NAME_POSITON].format(self.setupData.getName()))
        forged_list.append(self.contentList[10])
        forged_list.append(self.contentList[self.TEMPLATE_DESCRIPTION_POSITON].format(self.setupData.getDescription()))
        forged_list.append(self.contentList[12])
        forged_list.append(self.contentList[13])
        forged_list.append(self.contentList[self.TEMPLATE_KEYWORDS_POSITON].format(self.setupData.getKeywords()))
        forged_list.append(self.contentList[self.TEMPLATE_URL_POSITON].format(self.setupData.getUrl()))
        forged_list.append(self.contentList[self.TEMPLATE_AUTHOR_POSITION].format(self.setupData.getAuthor()))
        forged_list.append(self.contentList[self.TEMPLATE_AUTHOREMAIL_POSITION].format(self.setupData.getAuthorEmail()))
        forged_list.append(self.contentList[self.TEMPLATE_PACKAGE_POSITION].format(self.setupData.getPackage()))
        forged_list.append(
            self.contentList[19] + \
            self.contentList[self.TEMPLATE_ENTRYPOINTS_POSITION].format(
                self.setupData.getEntryPoint(),
                self.setupData.getPackage()
            ) + \
            self.contentList[21]
        )
        for oc in range(21, len(self.contentList)):
            forged_list.append(self.contentList[oc])

        self.contentList = forged_list

        # self.contentList[self.TEMPLATE_NAME_POSITON] =\
        #     self.contentList[self.TEMPLATE_NAME_POSITON].format(self.setupData.getName())

        # self.contentList[self.TEMPLATE_VERSION_POSITION] =\
        #     self.contentList[self.TEMPLATE_VERSION_POSITION].format(self.setupData.getVersion())
        #
        # self.contentList[self.TEMPLATE_DESCRIPTION_POSITON] = \
        #     self.contentList[self.TEMPLATE_DESCRIPTION_POSITON].format(self.setupData.getDescription())
        #
        # self.contentList[self.TEMPLATE_KEYWORDS_POSITON] = \
        #     self.contentList[self.TEMPLATE_KEYWORDS_POSITON].format(self.setupData.getKeywords())
        #
        # self.contentList[self.TEMPLATE_URL_POSITON] =\
        #     self.contentList[self.TEMPLATE_URL_POSITON].format(self.setupData.getUrl())
        #
        # self.contentList[self.TEMPLATE_AUTHOR_POSITION] = \
        #     self.contentList[self.TEMPLATE_AUTHOR_POSITION].format(self.setupData.getAuthor())
        #
        # self.contentList[self.TEMPLATE_AUTHOREMAIL_POSITION] = \
        #     self.contentList[self.TEMPLATE_AUTHOREMAIL_POSITION].format(self.setupData.getAuthorEmail())
        #
        # self.contentList[self.TEMPLATE_PACKAGE_POSITION] = \
        #     self.contentList[self.TEMPLATE_PACKAGE_POSITION].format(self.setupData.getPackage())
        #
        # self.contentList[self.TEMPLATE_ENTRYPOINTS_POSITION] = \
        #     self.contentList[self.TEMPLATE_ENTRYPOINTS_POSITION].format(self.setupData.getEntryPoint(), self.setupData.getPackage())

        return self

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
        contentList.append("VERSION = \"{0}\"")
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
        contentList.append("    entry_points={\"console_scripts\": ")
        contentList.append("[\"{0}={1}.__main__:main\"],")
        contentList.append("},")
        contentList.append("    include_package_data=True")
        contentList.append(")")

        return contentList
