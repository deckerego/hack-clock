#!/bin/sh

cd ..
echo "Compressing file..."
tar Jcf hackclock_2.0-beta.orig.tar.xz hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us
