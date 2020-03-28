#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaskcli", # Replace with your own username
    version="0.1.0",
    author="guxal",
    author_email="bitcoincucuta@gmail.com",
    description="CLI for create, manages, build and test your Flask projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guxal/Flask-CLI",
    packages=['flaskcli_pkg'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
    install_requires=[
        "typer>=0.0.8",
        "inflect>=4.1.0"
    ],
    scripts=['bin/flaskcli']
)
