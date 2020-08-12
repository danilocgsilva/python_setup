from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as file:
        return file.read()


setup(
    name="python_seytup",
    version=VERSION,
    description="Creates a template installable script in python.",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="python setup",
    url="https://github.com/danilocgsilva/python_setup",
    author="Danilo Silva",
    author_email="contato@danilocgsilva.me",
    packages=["setupPython"],
    entry_points={"console_scripts": ["spython=setupPython.__main__:main"]},
    include_package_data=True
)
