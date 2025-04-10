import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ksu_events',  # package import name
    version='0.1',
    packages= ['ksu_events', 'ksu_events.registration'],
    include_package_data=True,
    install_requires=[
        'django>=5',  # package requires django 5
    ],
    description='KSU Events Django package with shared code for KSU Events Django Projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alt-cs-lab/ksu-events',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',  # package requires python 3.10
)
