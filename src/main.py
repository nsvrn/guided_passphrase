
import numpy as np
import helper as hp
from get_wordlist import get_wordlist, WlType


def main():
    wltype = hp.select_wordlist()
    wordlist = get_wordlist(wltype)
    hp.print_intro(wltype, len(wordlist))
    rand_subset = []
    while len(rand_subset) < 100:
        rand_word = str(np.random.choice(wordlist))
        if rand_word not in rand_subset:
            rand_subset.append(rand_word)
    hp.print_grid(rand_subset)


if __name__ == '__main__':
    main()



