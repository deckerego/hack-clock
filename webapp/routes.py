#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger('hack-clock')

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from clock import Clock, ProcessStatus
from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, redirect, template

application = Bottle()
application.install(Clock())

@application.route('/favicon.ico')
def send_favicon():
	return static_file('favicon.ico', root='views/images')

@application.route('/js/<filename:path>')
def send_js(filename):
	return static_file(filename, root='views/js')

@application.route('/css/<filename:path>')
def send_css(filename):
	return static_file(filename, root='views/css')

@application.get('/')
def editor():
	redirect("/clock/edit")

@application.route('/codemirror/<filename:path>')
def send_js(filename):
	return static_file(filename, root='views/codemirror')

@application.post('/clock/restart')
def restart_event_loop(clock):
	clock.restart()
	return '{ "status": "restarted" }'

@application.get('/clock/status')
def status_event_loop(clock):
	return '{ "status": "%s" }' % clock.status()

@application.get('/clock/failures')
def status_stderr(clock):
	return clock.failures()

@application.get('/clock/edit')
def edit_event_loop(clock):
	code_file = open(clock.sourceFile, 'r')
	return template('editor', code=code_file.read(), status="Opened")

@application.post('/clock/edit')
def save_event_loop(clock):
	try:
		code_file = open(clock.sourceFile, 'w')
		code_file.write(request.forms.get('code'))

		clock.restart()

		code_file = open(clock.sourceFile, 'r')
		return template('editor', code=code_file.read(), status="Saved")
	except:
		return template('editor', code=request.forms.get('code'), status="Failed")
