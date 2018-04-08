import json
import os

ABBREVIATIONS_FILES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'Data', 'abbreviations')
ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'abbreviations.json')
PRIORITIZED_ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'prioritized_abbreviations.json')

with open(ABBREVIATIONS_DIR) as f:
    ABBREVIATIONS = json.load(f)
with open(PRIORITIZED_ABBREVIATIONS_DIR) as f:
    PRIORITIZED_ABBREVIATIONS = json.load(f)


def get_abbreviations():
    return ABBREVIATIONS


def get_prioritized_abbreviations():
    return PRIORITIZED_ABBREVIATIONS


def get_contractions():
    return __get_contractions(ABBREVIATIONS)


def get_priortized_contractions():
    return __get_contractions(PRIORITIZED_ABBREVIATIONS)


def __get_contractions(abbreviations: dict):
    contractions = dict()

    for key, value in abbreviations.items():
        contractions[value] = key

    return contractions
