
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Job Search Application'
LONG_DESCRIPTION = 'An application to auto search on LinkedIn for jobs based on filters.'

# Setting up
setup(
    name="JobSearchApp",
    version=VERSION,
    author="Boschetzel (Bogdan Fometescu)",
    author_email="<mbogdan.fometescu@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['selenium' ,'pyqt5'],
    keywords=['python', 'job search', 'pandas', 'selenium', 'linkedin'],
    url="https://github.com/Boschetzel/JobSearchProject",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
