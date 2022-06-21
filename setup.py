from setuptools import setup
import os

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="callofthevoid-example",
    version=os.environ["BUILD_BUILDNUMBER"],
    author="Rasmus Jørgensen",
    author_email="rasmus@callofthevoid.dk",
    description="An example of how to create and publish a Python package",
    packages=['callofthevoid_example'],
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
