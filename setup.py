from setuptools import setup, find_packages

setup(
    name="vacancy_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytest',
        'requests'
    ]
)