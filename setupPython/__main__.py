from setupPython.SetupData import SetupData
from setupPython.ContentTemplate import ContentTemplate
from setupPython.GenerateSetupContent import GenerateSetupContent


def main():

    setupData = SetupData()

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
    contentTemplate = ContentTemplate()
    contentTemplate.setSetupData(setupData)
    generate_setup_file = GenerateSetupContent()
    generate_setup_file.setContentTemplate(contentTemplate)
    setup_content = generate_setup_file.getSetupContent()
    print(setup_content)
