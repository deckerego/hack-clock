#!/bin/sh

VERSION='2.3.1'
ARCHP='armhf'

# Remove any testing files
rm -f home/pi/hack-clock/run_clock.py
rm -f home/pi/hack-clock/blocks_clock.xml
rm -f home/pi/hack-clock/backups/run_clock.*
rm -f home/pi/hack-clock/backups/blocks_clock.*

# Package
cd ..
echo "Compressing file..."
tar Jcf "hackclock_$VERSION.orig.tar.xz" hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us

# Cleanup
echo "Cleaning up artifacts..."
rm "../hackclock_$VERSION-1_$ARCHP.buildinfo"
rm "../hackclock_$VERSION-1_$ARCHP.changes"
rm "../hackclock_$VERSION-1.debian.tar.xz"
rm "../hackclock_$VERSION-1.dsc"
rm "../hackclock_$VERSION.orig.tar.xz"
