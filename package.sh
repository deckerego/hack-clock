#!/bin/sh

cd ..
echo "Compressing file..."
tar Jcf hackclock_2.0-pre.orig.tar.xz hack-clock/

cd hack-clock
dpkg-buildpackage -rfakeroot -uc -us
