import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instagramy",
    version="1.0.0",
    author="Yogeshwaran R",
    author_email="yogeshin247@gmail.com",
    description="Get Instagram user information ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogeshwaran01/instagramy/",
    packages=setuptools.find_packages(),
    download_url='https://github.com/yogeshwaran01/instagramy/archive/v_01.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['beautifulsoup4', 'requests']
)