import setuptools

with open("./README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="httpcats",
    version="1.1.1",
    author="itsmewulf",
    author_email="wulf.developer@gmail.com",
    description="Get URLs to your favourite HTTP Cats easily!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsmewulf/httpcats",
    keywords="cat, http, request, api, wrapper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
