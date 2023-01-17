from rich.console import Console
from rich.table import Table
# from rich.style import Style
import numpy as np
from get_wordlist import WlType
import math

console = Console()

def select_wordlist():
    txt = '''
    Select wordlist(0: EFF large, 1: BIP39, 2: Most-used-scrabble-words)
    Enter wordlist:'''
    wl = {0:WlType.EFFL, 1:WlType.BIP39, 2:WlType.MUSCRABBLE}
    console.print(txt, end='')
    inp = input()
    return wl[int(inp)]


def print_intro(wl, charset_len):
    console.print(f'\nwordlist: {wl.name}, charset-length: {charset_len}')
    console.print('Entropy: ', end='')
    for i in range(5, 11):
        b = math.floor(i * math.log(charset_len)/math.log(2))
        print(f'{i}-words: {b}b | ', end='')
    print('\n')


def print_grid(wordlist):
    colors = ['red', 'green', 'blue', 'yellow', 'black']
    table = Table(title="guided wordlist", show_header=False, show_lines=True)
    index = 0
    for _ in range(1, 11):
        fcolor = np.random.choice(colors)
        table.add_column('', justify="left", style=f'{fcolor}', no_wrap=True)
    for _ in range(1, 11):
        w = wordlist
        table.add_row(w[index], w[index+1], w[index+2], w[index+3], w[index+4], 
                        w[index+5], w[index+6], w[index+7], w[index+8],
                        w[index+9])
        index += 10
    console.print(table)