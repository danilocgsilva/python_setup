from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.GenerateReadmeContent import GenerateReadmeContent
from setupPython.GenerateStubScript import GenerateStubScript
from setupPython.Scaffold import Scaffold
import os


def main():
    setupData = SetupData()
    setupDataFilled = fillsSetupData(setupData)

    generate_readme_content = GenerateReadmeContent()
    generate_setup_content = GenerateSetupContent()
    generate_stub_content = GenerateStubScript()

    content_template = ContentTemplate().setSetupData(setupDataFilled)
    generate_setup_content.setContentTemplate(content_template)

    generate_readme_content.setTitle(setupData.getName())

    scaffold = Scaffold()
    scaffold.setBasePath(".")
    scaffold.setPackage(setupData.getPackage())
    scaffold.setReadmeContent(generate_readme_content.getContent())
    scaffold.setSetupContent(generate_setup_content.getContent())
    scaffold.setMainContent(generate_stub_content.getContent())
    scaffold.generate()


def fillsSetupData(setupData: SetupData):
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
