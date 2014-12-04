from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='landed_cost_pull_pi',
    version=version,
    description='pull purchase invoice',
    author='anton',
    author_email='anton@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
