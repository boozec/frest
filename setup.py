import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


def requirements():
    lines = []
    with open("requirements.txt") as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)

    return sorted(list(set(lines)))


setuptools.setup(
    name="frest",
    version="0.1.5",
    author="Santo Cariotti",
    description="Write REST API quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcariotti/frest",
    packages=setuptools.find_packages(),
    install_requires=requirements(),
    package_data={"frest": ["templates/*.txt"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=["bin/frest"],
)
