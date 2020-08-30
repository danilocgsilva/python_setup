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

    scaffold = Scaffold().setBasePath(".")

    setupDataFilled = fillsSetupData(SetupData())
    scaffold.setPackage(setupDataFilled.getPackage())

    generate_readme_content = GenerateReadmeContent().setTitle(setupDataFilled.getName())
    scaffold.setReadmeContent(generate_readme_content.getContent())

    content_template = ContentTemplate() \
        .setSetupData(setupDataFilled)
    generate_setup_content = GenerateSetupContent() \
        .setContentTemplate(content_template)
    scaffold.setSetupContent(generate_setup_content.getContent())
    generate_stub_content = GenerateStubScript()\
        .setTitle(setupDataFilled.getName())
    scaffold.setMainContent(generate_stub_content.getContent())
    generated_files = scaffold.generate()

    endMessages(generated_files, setupDataFilled)


def fillsSetupData(setupData: SetupData):
    packageName = input("Type the name for your package: ")
    setupData.setName(packageName)

    description = input("Type the description for your package: ")
    setupData.setDescription(description)

    keywords = input("Type some words to be the package keywords: ")
    setupData.setKeywords(keywords)

    url = input("Type the url for your project (you can paste the url here if you prefer): ")
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
    print("Now you can in your terminal:")
    print("```")
    print("pip3 install .")
    print(setup_data.getEntryPoint())
    print("```")
    print("And the things happens!")
    print("Next steps:")
    print("* Adjusts the content in the README.md to instruct better your script user.")
    print("* Develop everything in the " + setup_data.getPackage() + os.sep + "__main__.py script, then you see how the things are hapenning.")
    print("* Have the git installed, so you can do `git init` and starts to control your program version for better development.")