from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate
from setupPython.GenerateSetupContent import GenerateSetupContent
from setupPython.GenerateReadmeContent import GenerateReadmeContent
from setupPython.GenerateStubScript import GenerateStubScript
from setupPython.Scaffold import Scaffold
import os


def main():

    if len(os.listdir()) > 0:
        print("There are files in this folder.")
        print("Please, create an empty dir, go there and then you can create an installable Python script.")
        exit()

    setupData = SetupData()
    setupDataFilled = fillsSetupData(setupData)

    generate_readme_content = GenerateReadmeContent()
    generate_setup_content = GenerateSetupContent()
    generate_stub_content = GenerateStubScript()
    generate_stub_content.setTitle(setupData.getName())

    content_template = ContentTemplate().setSetupData(setupDataFilled)
    generate_setup_content.setContentTemplate(content_template)

    generate_readme_content.setTitle(setupData.getName())

    scaffold = Scaffold()
    scaffold.setBasePath(".")
    scaffold.setPackage(setupData.getPackage())
    scaffold.setReadmeContent(generate_readme_content.getContent())
    scaffold.setSetupContent(generate_setup_content.getContent())
    scaffold.setMainContent(generate_stub_content.getContent())
    generated_files = scaffold.generate()

    endMessages(generated_files, setupData)


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

    entry_points = input("Finally, type how you want to call your script: ")
    setupData.setEntryPoint(entry_points)

    return setupData

def endMessages(generated_files: list, setup_data: SetupData):
    print("Good! You just created the following files:")
    for file in generated_files:
        print("-> " + file)
    print("Next steps:")
    print("* Ajusts the README.md so clarify to others how to use your package.")
    print("* Starts your job altering the " + setup_data.getPackage() + os.sep + "__main__.py in the main() function. Everything starts there.")