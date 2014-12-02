import subprocess
import logging
import inspect

logger = logging.getLogger('clock')

class ProcessStatus():
    RUNNING = "running"
    TERMINATED = "terminated"
    NOT_STARTED = "not_started"

class Clock():
    name = 'clock'
    keyword = 'clock'
    sourceFile = '../runapp/run_clock.py'

    def __init__(self):
        self.eventLoop = None
        self.stderr = None

    def __del__(self):
        self.close()

    def status(self):
        if self.eventLoop:
            return ProcessStatus.TERMINATED if self.eventLoop.poll() else ProcessStatus.RUNNING
        else:
            return ProcessStatus.NOT_STARTED

    def stop(self):
        logger.info("Terminating clock event loop")
        self.eventLoop.terminate()

    def start(self):
        logger.info("Starting clock event loop")
        self.eventLoop = subprocess.Popen(["python", self.sourceFile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def restart(self):
        if self.status() == ProcessStatus.RUNNING:
            self.stop()
        self.start()

    def failures(self):
        if self.status() == ProcessStatus.TERMINATED and not self.stderr:
            self.stderr = self.eventLoop.stderr.read()
        elif self.status() != ProcessStatus.TERMINATED:
            self.stderr = None

        return self.stderr

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        logger.info("Loading clock event loop")

        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Clock):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of the clock driver running!")

        self.start()

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, context):
        conf = context.get('clock') or {}
        keyword = conf.get('keyword', self.keyword)

        args = inspect.getargspec(callback)[0]
        if keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = self
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

    # De-installation from Bottle as a plugin
    def close(self):
        self.stop()

class PluginError(Exception):
    pass

Plugin = Clock
