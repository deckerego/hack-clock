#!/bin/sh

rm home/pi/hack-clock/run_clock.py
rm home/pi/hack-clock/blocks_clock.xml
rm home/pi/hack-clock/backups/run_clock.*
rm home/pi/hack-clock/backups/blocks_clock.*

cd ..
echo "Compressing file..."
tar Jcf hackclock_2.2.2.orig.tar.xz hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us
