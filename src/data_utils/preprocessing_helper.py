import json
import os

ABBREVIATIONS_FILES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'Data', 'contractions')
ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'abbreviations.json')
PRIORITIZE_ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'prioritize_abbreviations.json')

with open(ABBREVIATIONS_DIR) as f:
    CONTRACTIONS = json.load(f)
with open(PRIORITIZE_ABBREVIATIONS_DIR) as f:
    PRIORITIZE_ABBREVIATIONS = json.load(f)

def get_abbreviations():
    return CONTRACTIONS

def get_prioritize_abbreviations():
    return PRIORITIZE_ABBREVIATIONS

def get_contractions():
    return __get_contractions(CONTRACTIONS)

def get_priortize_contractions():
    return __get_contractions(PRIORITIZE_ABBREVIATIONS)

def __get_contractions(abbreviations: dict):
    contractions = dict()

    for key, value in abbreviations.items():
        contractions[value] = key

    return contractions
