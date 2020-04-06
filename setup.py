import setuptools

setuptools.setup(
    name="frest",
    version="0.0.19",
    author="Santo Cariotti",
    description="Write REST API quickly",
    url="https://github.com/dcariotti/frest",
    packages=setuptools.find_packages(),
    package_data={"frest": ["templates/*.txt"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=["bin/frest"],
)
