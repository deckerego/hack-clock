#!/bin/sh

rm ~/.asoundrc
alsactl restore -i /etc/asound.conf 0
alsactl init -i /etc/asound.conf 0
amixer set Master -- 100%
speaker-test -c2 -twav
