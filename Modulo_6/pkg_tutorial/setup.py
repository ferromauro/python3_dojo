import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dojo-pgk-USERNAME", 
    version="0.0.1",
    author="YOUR NAME",
    author_email="mail@example.com",
    description="Put a simple description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="GIT HUB URL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)