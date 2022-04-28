from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="bosdyn-stubs",
    version="3.0.3",
    description="PEP 561 type stubs for bosdyn-api",
    url="https://github.com/elvout/bosdyn-stubs",
    install_requires=[
        "bosdyn-api>=3.0.3",
    ],
    packages=["bosdyn-stubs"],
    package_data=find_stubs("bosdyn-stubs"),
    classifiers=[
        "Typing :: Stubs Only",
    ]
)
