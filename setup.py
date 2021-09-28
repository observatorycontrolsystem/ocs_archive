from setuptools import setup

# Read the contents of the README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ocs_archive',
    version='0.1.0',
    description='Base library for the science archive and ingester of an observatory control system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/observatorycontrolsystem/ocs_archive',
    packages=['ocs_archive', 'ocs_archive.input', 'ocs_archive.settings', 'ocs_archive.storage'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    install_requires=[
        'astropy',
        'requests',
        'boto3',
        'python-dateutil',
        'lcogt-logging',
        'opentsdb-python-metrics>=0.2.0'
    ],
    extras_require={
        'tests': ['pytest']
    }
)
