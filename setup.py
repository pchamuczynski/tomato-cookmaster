from setuptools import setup, find_packages

setup(
    name="tomato-cookmaster",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.0.0",
        "openai>=0.10.5",
    ],
    author="Patryk Chamuczyński",
    author_email="p.chamuczynski@gmail.com",
    description="Tomato LLM assistant",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
