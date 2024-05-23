# Not yet in use


from setuptools import find_packages, setup

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="better-gym-cas",
    version="0.0.1",
    description="A better version of the python3 package gym-cas",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="test/markdown",
    url="https://github.com/ZBC-Slagelse-HTX-X/better-gym-cas",
    author="Jeppe Bøgeskov",
    license="MIT",
    classifiers=[
        "License :: MIT LICENSE",
        "Programing Language :: Python :: 3.12",
        "Operating System :: Arch Linux",
    ],
    # install_requires=["somePackage >= version"],
    # extras_require={
    #     "dev": ["somePackage>=version", "someOtherPackage>=version"],
    # },
    python_requires=">=3.10",
)