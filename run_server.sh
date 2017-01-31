#!/bin/sh

export PYTHONPATH="$PYTHONPATH:$HOME/Projects/hack-clock/lib"
cd srv/hackclock
../../scripts/run_server.py --config "$HOME/Projects/hack-clock/tests/localsettings.conf"
