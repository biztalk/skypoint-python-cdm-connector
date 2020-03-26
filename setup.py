from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="cdm-connector",
    version="0.0.1",
    description="A Python package to read and write files in CDM format. Customized for SkyPoint use cases.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/skypointcloud/skypoint-python-cdm-connector",
    author="SkyPoint Cloud",
    author_email="support@skypointcloud.com",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: LGPL License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["skypoint-python-cdm"],
    include_package_data=True,
    install_requires=["requests"]
)