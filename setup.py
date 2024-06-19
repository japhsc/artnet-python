from setuptools import find_packages, setup

setup(
    name="artnet-python",
    version="0.0.1",
    author="Jan-Philipp Schröder",
    author_email="jan.philipp.s@gmail.com",
    description="Artnet library",
    long_description=(
        "Library for sending and receiving ArtNet 4 (protocol 14) packages"
    ),
    packages=find_packages(),
    install_requires=[],
)
