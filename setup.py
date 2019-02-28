import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TCPFestival",
    version="0.1",
    author="Santiago Buczak",
    author_email="the.elven.archer@gmail.com",
    description="A Network Festival TTS Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/the-elven-archer/TCPFestival",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
)
