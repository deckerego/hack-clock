#!/usr/bin/env python

from distutils.core import setup
import os

setup(
    name='HackClock',
    version='2.0-BETA',
    description='A hackable alarm clock for the Raspberry Pi',
    author='DeckerEgo',
    author_email='john@deckerego.net',
    url='http://hackclock.deckerego.net/',
    long_description=open('README.md').read(),
    packages=['runapp', 'webapp'],
    package_dir={
        'runapp': 'runapp',
        'webapp': 'webapp'
    },
    package_data={
        'runapp': ['audio/*', 'backups/README.md', 'lessons/*'],
        'webapp': ['views/*']
    },
    data_files=[
        ('/etc/init.d',    ['debian/etc/init.d/hack-clock'])
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education"
    ],
    keywords='alarm clock raspberry pi rpi hardware python learning blocks blockly diy hackclock hack hardware',
    requires=[
        'bitstring (>=3.1.3)',
        'wiringpi2 (>=1.0.10)',
        'bottle (>=0.12.7)'
    ],
)
