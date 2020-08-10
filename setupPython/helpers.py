def getContentTemplateList() -> list:

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
    contentList.append("    keywords=\"{0},\"")
    contentList.append("    url=\"{0}\",")
    contentList.append("    author=\"{0}\",")
    contentList.append("    author_email=\"{0}\",")
    contentList.append("    packages=[\"{0}\"],")
    contentList.append("    entry_points={\"console_scripts\": [\"{0}={1}.__main__:main\"],},")
    contentList.append("    include_package_data=True")
    contentList.append(")")

    return contentList
