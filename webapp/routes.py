#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger('hack-clock')

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
logger.addHandler(console)

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from dateutil import parser
from datetime import datetime
from config import configuration
from clock import Clock, ProcessStatus
from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, redirect, template
from os import listdir

application = Bottle()
application.install(Clock())

@application.get('/')
def editor():
    return template('index')

@application.route('/favicon.ico')
def send_favicon():
    return static_file('favicon.ico', root='views/images')

@application.route('/js/<filename:path>')
def send_js(filename):
    return static_file(filename, root='views/js')

@application.route('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='views/css')

# Python Editing
@application.route('/codemirror/<filename:path>')
def send_codemirror(filename):
    return static_file(filename, root='views/codemirror')

@application.get('/python/css/<filename:path>')
def send_python_css(filename):
    return static_file(filename, root='views/python/css')

@application.get('/python/edit')
def edit_event_loop(clock):
    try:
        code_file = open(clock.sourceFile, 'r')
        return template('python/editor', code=code_file.read(), status="Opened")
    except Exception as ex:
        logger.error(ex)
        return template('python/editor', code='', status="Opened")

# Blockly Editing
@application.route('/blockly/<filename:path>')
def send_blockly(filename):
    return static_file(filename, root='views/blockly')

@application.get('/blocks/css/<filename:path>')
def send_blocks_css(filename):
    return static_file(filename, root='views/blocks/css')

@application.get('/blocks/js/<filename:path>')
def send_blocks_js(filename):
    return static_file(filename, root='views/blocks/js')

@application.get('/blocks/edit')
def edit_event_loop(clock):
    try:
        blocks_file = configuration.get('blocks_file')
        code_file = open(blocks_file, 'r')
        return template('blocks/editor', blocks_state=code_file.read(), status="Opened")
    except Exception as ex:
        logger.error(ex)
        return template('blocks/editor', blocks_state='', status="Opened")

@application.put('/blocks/save')
def save_event_loop(clock):
    version_dir = configuration.get('backup_files')
    backup_name = "%s/blocks_clock.%s" % (version_dir, datetime.now().isoformat())
    blocks_state = request.body.read()

    try:
        blocks_file = configuration.get('blocks_file')

        # Save backup
        code_file = open(blocks_file, 'r')
        backup_file = open(backup_name, 'w')
        backup_file.write(code_file.read())
    except Exception as ex:
        logger.error(ex)

    try:
        # Save file
        code_file = open(blocks_file, 'w')
        code_file.write(blocks_state)

        # Load saved file
        code_file = open(blocks_file, 'r')
        return code_file.read()
    except Exception as ex:
        logger.error(ex)
        return blocks_state

# Clock REST API
@application.put('/clock/code')
def save_event_loop(clock):
    version_dir = configuration.get('backup_files')
    backup_name = "%s/run_clock.%s" % (version_dir, datetime.now().isoformat())
    source_text = request.body.read()

    try:
        # Save backup
        code_file = open(clock.sourceFile, 'r')
        backup_file = open(backup_name, 'w')
        backup_file.write(code_file.read())
    except Exception as ex:
        logger.error(ex)

    try:
        # Save file
        code_file = open(clock.sourceFile, 'w')
        code_file.write(source_text)

        clock.restart()

        # Load saved file
        code_file = open(clock.sourceFile, 'r')
        return code_file.read()
    except Exception as ex:
        logger.error(ex)
        return source_text

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

# File Asset Upload
@application.post('/audio')
def audio_upload():
    uploaded = request.files.get('upload')
    audio_dir = configuration.get('audio_files')
    uploaded.save(audio_dir)
    redirect("/audio")

@application.get('/audio')
def audio_list():
    audio_dir = configuration.get('audio_files')
    files = listdir(audio_dir)
    return template('audio', files=files)

# Backup / Restore
@application.get('/clock/code/backups')
def backup_list(clock):
    version_dir = configuration.get('backup_files')
    lesson_dir = configuration.get('lesson_files')
    files = listdir(version_dir)

    lessons = [
        ("1", "Lesson One: Light up the clock", open("%s/1/run_clock.py" % lesson_dir, 'r').read()),
        ("2", "Lesson Two: Hours and minutes", open("%s/2/run_clock.py" % lesson_dir, 'r').read()),
        ("3", "Lesson Three: AM/PM indicator", open("%s/3/run_clock.py" % lesson_dir, 'r').read()),
        ("4", "Lesson Four: Play music!", open("%s/4/run_clock.py" % lesson_dir, 'r').read()),
        ("5", "Lesson Five: Show the current temperature", open("%s/5/run_clock.py" % lesson_dir, 'r').read()),
        ("6", "Lesson Six: Loading configuration settings", open("%s/6/run_clock.py" % lesson_dir, 'r').read()),
        ("final", "Final Lesson: Putting it all together", open("%s/final/run_clock.py" % lesson_dir, 'r').read()),
        ("musiclover", "Example: A music lover's clock", open("%s/musiclover/run_clock.py" % lesson_dir, 'r').read())
    ]

    backups = []
    for filename in files:
        backup_name = "%s/%s" % (version_dir, filename)
        diff = open(backup_name, 'r').read()

        try:
            filetime = parser.parse(filename.lstrip("run_clock."))
            backups.append((filetime.strftime("%s"), filetime.strftime("%Y-%m-%d"), filetime.strftime("%H:%M:%S"), diff, filename))
        except:
            logger.warn("Could not parse file %s" % filename)

    return template('backups', backups=backups, lessons=lessons)

@application.get('/clock/code/lesson/<file_id:int>')
def lesson_event_loop(clock, file_id):
    lesson_dir = configuration.get('lesson_files')
    lesson_file = "%s/%s/run_clock.py" % (lesson_dir, file_id)

    try:
        code_file = open(lesson_file, 'r')
        return template('editor', code=code_file.read(), status="Saved")
    except:
        return template('editor', code=request.forms.get('code'), status="Failed")

@application.get('/clock/code/restore/<file_id:int>')
def restore_event_loop(clock, file_id):
    version_dir = configuration.get('backup_files')
    files = listdir(version_dir)
    restored_files = filter(lambda f: int(parser.parse(f.lstrip("run_clock.")).strftime("%s")) == file_id, files)
    restored_file = "%s/%s" % (version_dir, restored_files[0])

    try:
        # Load saved file
        code_file = open(restored_file, 'r')
        return template('editor', code=code_file.read(), status="Saved")
    except:
        return template('editor', code=request.forms.get('code'), status="Failed")
