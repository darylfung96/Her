import json
import os

DATA_SETTINGS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json')
with open(DATA_SETTINGS_DIR) as f:
    DATA_SETTINGS = json.load(f)