#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from hackclock.webapp.routes import application
from bottle import run
from hackclock.config import configuration

os.chdir(configuration.get('webapp_files'))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 9003))
	run(application, reloader = False, host = '0.0.0.0', port = port, quiet = False)
	application.close()
