from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.GenerateReadmeContent import GenerateReadmeContent
from setupPython.GenerateStubScript import GenerateStubScript
import os


def main():

    setupData = SetupData()
    setupDataFilled = fillsSetupData(setupData)

    generate_readme_content = GenerateReadmeContent()
    generate_setup_content = GenerateSetupContent()
    generate_stub_content = GenerateStubScript()

    content_template = ContentTemplate().setSetupData(setupDataFilled)
    generate_setup_content.setContentTemplate(content_template)




def fillsSetupData(self, setupData: SetupData):
    packageName = input("Type the name for your package: ")
    setupData.setName(packageName)

    description = input("Type the description for your package: ")
    setupData.setDescription(description)

    keywords = input("Type some words to be the package keywords: ")
    setupData.setKeywords(keywords)

    url = input("Type (paste) the url for your project: ")
    setupData.setUrl(url)

    author = input("Type the author of your package: ")
    setupData.setAuthor(author)

    author_email = input("Set the author e-mail: ")
    setupData.setAuthorEmail(author_email)

    package_identifier = input("Write the name acessible by the system (think as system namespace): ")
    setupData.setPackage(package_identifier)

    entry_points = input("Finally, type how you want to call your script: ")
    setupData.setEntryPoint(entry_points)

    return setupData
