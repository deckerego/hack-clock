#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import os

def all_files(newroot, oldroot):
    fdtuples = []
    for root, dirs, files in os.walk(oldroot):
        fds = []
        for fd in files:
            if not fd[0] is '.':
                fds.append(os.path.join(root, fd))
        relpath = os.path.relpath(root, oldroot)
        fdtuple = (os.path.join(newroot, relpath), fds)
        fdtuples.append(fdtuple)
    return fdtuples

base_data_files = [
    ('/etc',    ['etc/hack-clock.conf', 'etc/asound.conf']),
    ('/etc/init.d',    ['etc/init.d/hack-clock']),
    ('/etc/default',    ['etc/default/hack-clock']),
    ('/usr/share/doc/hack-clock', ['README.md', 'LICENSE', 'MANIFEST', 'requirements.txt'])
]
webapp_data_files = all_files('/srv/hackclock', 'srv/hackclock')
runapp_data_files = all_files('/home/pi/hack-clock', 'home/pi/hack-clock')

setup(
    name='HackClock',
    version='2.3.1',
    description='A hackable alarm clock for the Raspberry Pi',
    author='DeckerEgo',
    author_email='john@deckerego.net',
    url='http://hackclock.deckerego.net/',
    long_description=open('README.md').read(),
    packages=[
        'hackclock',
        'hackclock.runapp',
        'hackclock.runapp.Adafruit',
        'hackclock.runapp.Libs',
        'hackclock.webapp',
    ],
    package_dir={
        '': 'lib'
    },
    package_data={
        'hackclock': [
            'lessons/**/*'
        ]
    },
    data_files=(base_data_files + webapp_data_files + runapp_data_files),
    scripts=[
        'scripts/run_server.py'
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Topic :: Education"
    ],
    keywords='alarm clock raspberry pi rpi hardware python learning blocks blockly diy hackclock hack hardware',
    requires=[
        'bitstring (>=3.1.3)',
        'wiringpi2 (>=2.23.1)',
        'bottle (>=0.12.7)',
        'gmusicapi (>=10.1.0)'
    ],
)
