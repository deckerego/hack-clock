import argparse

config_values = {
    'python_file': '../runapp/run_clock.py',
    'blocks_file': '../runapp/blocks_clock.xml',
    'audio_files': '../runapp/audio',
    'backup_files': '../runapp/backups',
    'lesson_files': '../runapp/lessons',
    'file_filter': ['README.md', '.DS_Store'],
    'buttons_gpio': [24],
    'switches_gpio': []
}

class Configuration(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        args, _ = parser.parse_known_args()

    def get(self, name):
        return config_values.get(name)

configuration = Configuration()
