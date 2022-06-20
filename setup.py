from setuptools import setup
import os

with open("Readme.md", "r") as fh:
    long_description = fh.read()

for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))

setup(
    name="python-package-example",
    version=os.environ["Build_BuildNumber"],
    author="Rasmus Jørgensen",
    author_email="rasmus@callofthevoid.dk",
    description="An example of how to create and publish a Python package",
    packages=['test_package'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
