from setuptools import setup, find_packages

setup(
    name='ksu-events',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=5',
    ],
    description='KSU Events Django package with shared code for KSU Events Django Projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zombiepaladin/ksu-events',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
)
