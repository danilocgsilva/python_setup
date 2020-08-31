class Mocking:

    def getFullSample(self):
        return '''from setuptools import setup

VERSION = "2.2.1"

def readme():
    with open(\"README.md\") as f:
        return f.read()

setup(
    name="my-app-name",
    version=VERSION,
    description="This is the description of my application.",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="those are the keywords",
    url="http://thisistheversioncontrol.site",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["thepackage"],
    entry_points={"console_scripts": ["executehere=thepackage.__main__:main"],},
    include_package_data=True
)
'''

    def getSampleWithoutEntryPoint(self):
        return '''from setuptools import setup

VERSION = "2.2.1"

def readme():
    with open(\"README.md\") as f:
        return f.read()

setup(
    name="my-app-name",
    version=VERSION,
    description="This is the description of my application.",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="those are the keywords",
    url="http://thisistheversioncontrol.site",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["thepackage"],
    include_package_data=True
)
'''
