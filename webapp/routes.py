#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger('hack-clock')

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, template

application = Bottle()

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
  return template('index')

@application.route('/codemirror/<filename:path>')
def send_js(filename):
  return static_file(filename, root='views/codemirror')

@application.get('/edit/run_clock.py')
def editor():
  code_file = open('../runapp/run_clock.py', 'r')
  return template('editor', code=code_file.read(), status="Opened")

@application.post('/edit/run_clock.py')
def save_file():
	try:
		code_file = open('../runapp/run_clock.py', 'w')
		code_file.write(request.forms.get('code'))

		code_file = open('../runapp/run_clock.py', 'r')
		return template('editor', code=code_file.read(), status="Saved")
	except:
		return template('editor', code=request.forms.get('code'), status="Failed")
