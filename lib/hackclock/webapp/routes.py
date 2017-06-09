#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import json

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger('hack-clock')

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
logger.addHandler(console)

import urllib
from dateutil import parser
from datetime import datetime
from hackclock.config import configuration
from clock import Clock, ProcessStatus
from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, redirect, template, error
from os import listdir
import re

application = Bottle()
application.install(Clock())

@application.get('/')
def home():
    default_editor = configuration.get('default_editor')
    is_deps_missing = False

    try:
        import wiringpi
        import bitstring
    except(ImportError):
        is_deps_missing = True

    fs_stats = os.statvfs(configuration.get('audio_files'))
    free_percent = (fs_stats.f_bavail * 100) / fs_stats.f_blocks

    return template('index', edit_path=default_editor, missing_deps=is_deps_missing, disk_free=free_percent)

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

@application.get('/python/js/<filename:path>')
def send_python_css(filename):
    return static_file(filename, root='views/python/js')

@application.get('/python/edit')
def python_edit_event_loop(clock):
    switch_visible = not configuration.get('disable_editor_button')
    return template('python/editor', switch_visible=switch_visible, status="Opened")

@application.get('/python/read')
def python_edit_event_loop(clock):
    try:
        code_file = open(clock.sourceFile, 'r')
        return code_file.read()
    except Exception as ex:
        logger.error(ex)
        return ''

@application.put('/python/save')
def python_save_event_loop(clock, body=None):
    version_dir = configuration.get('backup_files')
    backup_name = "%s/run_clock.%s" % (version_dir, datetime.now().isoformat())
    source_text = body.read() if body else request.body.read()

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

# Python Backup / Restore
@application.get('/python/backups')
def python_backup_list(clock):
    version_dir = configuration.get('backup_files')
    lesson_dir = configuration.get('lesson_files')
    python_file_re = re.compile('run_clock.*')
    files = sorted(filter(python_file_re.match, listdir(version_dir)), reverse=True)

    lessons = [
        ("1", "Lesson One: Light up the clock", open("%s/1/run_clock.py" % lesson_dir, 'r').read()),
        ("2", "Lesson Two: Hours and minutes", open("%s/2/run_clock.py" % lesson_dir, 'r').read()),
        ("3", "Lesson Three: AM/PM indicator", open("%s/3/run_clock.py" % lesson_dir, 'r').read()),
        ("4", "Lesson Four: Play music!", open("%s/4/run_clock.py" % lesson_dir, 'r').read()),
        ("5", "Lesson Five: Adding buttons to push", open("%s/5/run_clock.py" % lesson_dir, 'r').read()),
        ("6", "Lesson Six: Show the temperature outside", open("%s/6/run_clock.py" % lesson_dir, 'r').read()),
        ("final", "Final Lesson: Putting it all together", open("%s/final/run_clock.py" % lesson_dir, 'r').read()),
        ("musiclover", "Example: A music lover's clock", open("%s/musiclover/run_clock.py" % lesson_dir, 'r').read()),
        ("gpio", "Example: Using switches and buttons", open("%s/gpio/run_clock.py" % lesson_dir, 'r').read())
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

    return template('python/backups', backups=backups, lessons=lessons)

@application.get('/python/lesson/<file_id>')
def python_lesson_event_loop(clock, file_id):
    lesson_dir = configuration.get('lesson_files')
    lesson_file = "%s/%s/run_clock.py" % (lesson_dir, file_id)
    switch_visible = not configuration.get('disable_editor_button')

    try:
        code_file = open(lesson_file, 'r')
        python_save_event_loop(clock, code_file)
        return template('python/editor', switch_visible=switch_visible, status="Opened")
    except:
        return template('python/editor', switch_visible=switch_visible, status="Failed")

@application.get('/python/restore/<file_id:int>')
def python_restore_event_loop(clock, file_id):
    version_dir = configuration.get('backup_files')
    files = listdir(version_dir)
    restored_files = filter(lambda f: f.startswith('run_clock.') and int(parser.parse(f.lstrip("run_clock.")).strftime("%s")) == file_id, files)
    restored_file = "%s/%s" % (version_dir, restored_files[0])
    switch_visible = not configuration.get('disable_editor_button')

    try:
        code_file = open(restored_file, 'r')
        python_save_event_loop(clock, code_file)
        return template('python/editor', switch_visible=switch_visible, status="Opened")
    except:
        return template('python/editor', switch_visible=switch_visible, status="Failed")

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
def blocks_edit_event_loop(clock):
    switch_visible = not configuration.get('disable_editor_button')
    google_music = configuration.get('google_username') and configuration.get('google_password')
    ifttt_maker = configuration.get('ifttt_maker_key')

    return template('blocks/editor', switch_visible=switch_visible, google_music=google_music, ifttt_maker=ifttt_maker, status="Opened")

@application.get('/blocks/read')
def blocks_read_event_loop(clock):
    try:
        blocks_file = configuration.get('blocks_file')
        code_file = open(blocks_file, 'r')
        return code_file.read()
    except Exception as ex:
        logger.error(ex)
        return ''

@application.put('/blocks/save')
def blocks_save_event_loop(clock, body=None):
    version_dir = configuration.get('backup_files')
    backup_name = "%s/blocks_clock.%s" % (version_dir, datetime.now().isoformat())
    blocks_state = body.read() if body else request.body.read()

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

# Blocks Backup / Restore
@application.get('/blocks/backups')
def blocks_backup_list(clock):
    version_dir = configuration.get('backup_files')
    lesson_dir = configuration.get('lesson_files')
    block_file_re = re.compile('blocks_clock.*')
    files = sorted(filter(block_file_re.match, listdir(version_dir)), reverse=True)

    lessons = [
        ("1", "Lesson One: Light up the clock", open("%s/1/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("2", "Lesson Two: Hours and minutes", open("%s/2/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("3", "Lesson Three: AM/PM indicator", open("%s/3/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("4", "Lesson Four: Play music!", open("%s/4/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("5", "Lesson Five: Adding buttons to push", open("%s/5/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("6", "Lesson Six: Show the temperature outside", open("%s/6/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("final", "Final Lesson: Putting it all together", open("%s/final/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("musiclover", "Example: A music lover's clock", open("%s/musiclover/blocks_clock.xml" % lesson_dir, 'r').read()),
        ("gpio", "Example: Using switches and buttons", open("%s/gpio/blocks_clock.xml" % lesson_dir, 'r').read())
    ]

    backups = []
    for filename in files:
        backup_name = "%s/%s" % (version_dir, filename)
        diff = open(backup_name, 'r').read()

        try:
            filetime = parser.parse(filename.lstrip("blocks_clock.xml."))
            backups.append((filetime.strftime("%s"), filetime.strftime("%Y-%m-%d"), filetime.strftime("%H:%M:%S"), diff, filename))
        except:
            logger.warn("Could not parse file %s" % filename)

    return template('blocks/backups', backups=backups, lessons=lessons)

@application.get('/blocks/lesson/<file_id>')
def blocks_lesson_event_loop(clock, file_id):
    lesson_dir = configuration.get('lesson_files')
    lesson_file = "%s/%s/blocks_clock.xml" % (lesson_dir, file_id)

    switch_visible = not configuration.get('disable_editor_button')
    google_music = configuration.get('google_username') and configuration.get('google_password')
    ifttt_maker = configuration.get('ifttt_maker_key')

    try:
        code_file = open(lesson_file, 'r')
        blocks_save_event_loop(clock, code_file)
        return template('blocks/editor', switch_visible=switch_visible, google_music=google_music, ifttt_maker=ifttt_maker, status="Opened")
    except:
        return template('blocks/editor', switch_visible=switch_visible, google_music=google_music, ifttt_maker=ifttt_maker, status="Failed")

@application.get('/blocks/restore/<file_id:int>')
def blocks_restore_event_loop(clock, file_id):
    version_dir = configuration.get('backup_files')
    files = listdir(version_dir)
    restored_files = filter(lambda f: f.startswith('blocks_clock.') and int(parser.parse(f.lstrip("blocks_clock.")).strftime("%s")) == file_id, files)
    restored_file = "%s/%s" % (version_dir, restored_files[0])

    switch_visible = not configuration.get('disable_editor_button')
    google_music = configuration.get('google_username') and configuration.get('google_password')
    ifttt_maker = configuration.get('ifttt_maker_key')

    try:
        code_file = open(restored_file, 'r')
        blocks_save_event_loop(clock, code_file)
        return template('blocks/editor', switch_visible=switch_visible, google_music=google_music, ifttt_maker=ifttt_maker, status="Opened")
    except:
        return template('blocks/editor', switch_visible=switch_visible, google_music=google_music, ifttt_maker=ifttt_maker, status="Failed")

# Clock REST API
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

def audio_files():
    audio_dir = configuration.get('audio_files')
    filename_filter = configuration.get('file_filter')
    return filter(lambda e: e not in filename_filter, listdir(audio_dir))

@application.get('/audio')
def audio_view():
    fs_stats = os.statvfs(configuration.get('audio_files'))
    free_mb = (fs_stats.f_bavail * fs_stats.f_frsize) / (1024**2)
    full_percent = 100 - ((fs_stats.f_bavail * 100) / fs_stats.f_blocks)
    is_full = free_mb < 20
    return template('audio', files=audio_files(), free_space=free_mb, percent_full=full_percent, is_full=is_full)

@application.get('/audio/list')
def audio_list():
    return json.dumps(audio_files())

@application.delete('/audio/<file_id>')
def delete_audio_file(file_id):
    audio_dir = configuration.get('audio_files')
    file_name = urllib.unquote(file_id)
    file_path = "%s/%s" % (audio_dir, file_name)

    response = {}
    response['path'] = file_path
    response['status'] = 'none'

    try:
        os.remove(file_path)
        response['status'] = 'deleted'
    except EnvironmentError as ex:
        response['status'] = 'failed'
        response['error'] = str(ex)

    return json.dumps(response)

# GPIO pin list
@application.get('/gpio/button/list')
def button_list():
    button_pins = configuration.get('buttons_gpio')
    return json.dumps(button_pins)

@application.get('/gpio/switch/list')
def switch_list():
    switch_pins = configuration.get('switches_gpio')
    return json.dumps(switch_pins)

# Weather Station
@application.get('/weather/station/id')
def weather_list():
    switch_pins = configuration.get('switches_gpio')
    return json.dumps(switch_pins)

@application.error(404)
def notfound_page(error):
    return home()

@application.error(500)
def error_page(error):
    default_editor = configuration.get('default_editor')
    error_message = error.exception
    page = '''
        <!doctype html>
        <html>
        <head>
          <meta charset="utf-8">
          <title>Welcome to Hack Clock</title>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
          <link rel="stylesheet" href="/css/styles.css?v=2" type="text/css" />
        </head>
        <body>
          <div class="container">

            <nav class="navbar navbar-default navbar-static-top" role="navigation">
              <div class="container-fluid">
                <div class="navbar-header">
                  <a class="navbar-brand" href="http://hackclock.deckerego.net/">Hack Clock</a>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                  <ul class="nav navbar-nav">
                    <li class="active"><a href="/">Home</a></li>
                    <li><a href="%s">Edit Code</a></li>
                    <li><a href="/audio">Upload Audio</a></li>
                  </ul>
                </div>
              </div>
            </nav>

            <div class="jumbotron">
              <div class="page-header">
                <h1>D'oh! My Bad...</h1>
                <p class="lead">There was an error in the Hack Clock webapp!</p>
                <p>
                  Let us know by
                  <a href="https://github.com/deckerego/hack-clock/issues/new">submitting an issue</a>
                  with the error below:
                </p>
              </div>
              <div class="alert alert-danger" role="alert">
                <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                %s
              </div>
            </div>

          </div>
        </body>
        </html>
    '''
    return page % (default_editor, error_message)
