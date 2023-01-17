from enum import Enum
from pathlib import Path
from numpy import loadtxt


class WlType(Enum):
    MUSCRABBLE = 0
    EFFL = 1
    BIP39 = 2


def _fpath(f):
    fpath = Path(__file__).parents[1].joinpath('wordlists').joinpath(f)
    return fpath


def get_wordlist(wltype: WlType):
    wl = None
    if wltype == WlType.MUSCRABBLE:
        wl = get_muscrabble()
    elif wltype == WlType.EFFL:
        wl = get_eff_list()
    elif wltype == WlType.BIP39:
        wl = get_bip39_list()
    return wl


def get_eff_list():
    words = []
    f = 'eff_large.txt'
    words = loadtxt(_fpath(f), dtype=str, unpack=True)[1]
    return words

def get_bip39_list():
    words = []
    f = 'bip39.txt'
    words = loadtxt(_fpath(f), dtype=str, unpack=False)
    return words


def get_muscrabble():
    '''
        Peter Norvig's most used ngram list of 300k words
            intersection with scrabble sowpod wordlist
    '''
    words = []
    s, n = 'sowpods_wordlist.txt', 'norvig_ngram.txt'
    sowpod_words = loadtxt(_fpath(s), dtype=str, unpack=False)
    ngram_words = loadtxt(_fpath(n), dtype=str, unpack=True)[0]
    words = list(set(sowpod_words) & set(ngram_words))
    return words