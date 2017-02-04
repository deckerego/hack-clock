#!/bin/sh

cd ..
echo "Compressing file..."
tar Jcf hackclock_2.1.0.orig.tar.xz hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us
