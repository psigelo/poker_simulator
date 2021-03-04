
from setuptools import find_packages, setup

setup(
    name="poker_simulator",
    version='1.0',
    packages=find_packages(exclude=['config,static,templates']),
    zip_safe=True,
    decription='',
    entry_points={}
)

