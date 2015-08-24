#!/usr/bin/env python
#
# Copyright 2015 Evan Gray
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import sys

from setuptools import setup, find_packages


install_requires = ['slackclient']
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='paperslacktail',
    version='1.0.3',
    author='Evan Gray',
    author_email='hello@evanscottgray.com',
    description='stream from papertrail into slack.',
    long_description=open('README.rst').read(),
    keywords=['slack', 'papertrail'],
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Apache Software License'],
    license='Apache Software License',
    url='https://github.com/evanscottgray/paperslacktail',
    entry_points={
        'console_scripts': [
            'paperslacktail = paperslacktail.paperslacktail:main']})
