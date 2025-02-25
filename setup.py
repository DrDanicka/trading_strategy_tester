from setuptools import setup, find_packages

requirements = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='trading_strategy_tester',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements
)
