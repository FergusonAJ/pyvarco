import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvarco-FergusonAJ", # Replace with your own username
    version="0.1.0",
    author="Austin Ferguson",
    author_email="ferguson.austin.j@gmail.com",
    description="Creates all combinations of the variables specified.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FergusonAJ/pyvarco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
