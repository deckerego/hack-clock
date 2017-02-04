#!/bin/sh

rm home/pi/hack-clock/run_clock.py
rm home/pi/hack-clock/blocks_clock.xml
rm home/pi/hack-clock/backups/*

cd ..
echo "Compressing file..."
tar Jcf hackclock_2.1.0.orig.tar.xz hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us
