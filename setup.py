from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list[str]:
    with open(file_path) as f:
        return [
            line.strip() for line in f
            if line.strip() and not line.startswith("#") and line.strip() != "-e ."
        ]

setup(
    name='my_package',
    version='0.1.0',
    author='Kartheek',
    author_email='vksorbit1@gmail.com',
    packages=find_packages(),       
    install_requires=get_requirements('requirements.txt'),
)