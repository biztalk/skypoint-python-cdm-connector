from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="cdm-connector",
    version="0.0.1",
    description="A Python package to read and write files in CDM format",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/skypointcloud/skypoint-python-cdm-connector",
    author="SkyPoint Cloud",
    author_email="support@skypointcloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["skypoint-python-cdm"],
    include_package_data=True,
    install_requires=["requests"]
)