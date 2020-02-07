import pickle
from collections import defaultdict

from aaransia.aramorpher import Morpheme, Aramorpher
from aaransia.process_files import process_textfile, process_tableXY
from aaransia.constants import *

prefixes = defaultdict(list)
stems    = defaultdict(list)
suffixes = defaultdict(list)

ab = defaultdict(list)
bc = defaultdict(list)
ac = defaultdict(list)

def process_prefixes():
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(BASE_DIR + DATA_DIR + DICT_PREFIXES):
        prefixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))

def process_stems():
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(BASE_DIR + DATA_DIR + DICT_STEMS):
        stems[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))

def process_suffixes():
    for (unvowelled, vowelled, cat, pos, gloss, root) in process_textfile(BASE_DIR + DATA_DIR + DICT_SUFFIXES):
        suffixes[unvowelled].append(Morpheme(vowelled, cat, pos, gloss, root))

def process_tableAB():
    for (left, right) in process_tableXY(BASE_DIR + DATA_DIR + TABLE_AB):
        ab[left].append(right)

def process_tableBC():
    for (left, right) in process_tableXY(BASE_DIR + DATA_DIR + TABLE_BC):
        bc[left].append(right)

def process_tableAC():
    for (left, right) in process_tableXY(BASE_DIR + DATA_DIR + TABLE_AC):
        ac[left].append(right)

def make_pickle():
    process_prefixes()
    process_stems()
    process_suffixes()
    process_tableAB()
    process_tableBC()
    process_tableAC()

    # now construct AramorphInfo
    aramorph = Aramorpher(prefixes, stems, suffixes, ab, bc, ac)

    # and pickle it
    pickle.dump(aramorph, open(BASE_DIR + DATA_DIR + ANAMORPH_DATA, "wb"), pickle.HIGHEST_PROTOCOL)