from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="project_processamento",
    version="0.0.1",
    author="Mauricio",
    author_email="mauricio.oliveira8583@gmail.com",
    description="Primeiro projeto",
    long_description=page_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/Mauricio8583/Pacotes_processamento_python",
    packages=find_packages(),
    install_requires= requirements,
    python_requires= ">=3.8",
)