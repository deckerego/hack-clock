#!/bin/sh

rm ~/.asoundrc
amixer set Master -- 100%
speaker-test -c2 -twav
