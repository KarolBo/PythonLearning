# Frozen sets
fs = frozenset({'a', 'b', 'c'})
print(fs)
# fs.add('c')

# Rounding numbers
pi = 3.14159
print(f'{pi:.2f} {pi:.2g}')

# Negative decimal rounding
x = 1234.567
print(round(x, -1))

# Color prints
from colorama import Fore
print(Fore.RED + 'This text is printed in red ' + Fore.BLUE + 'and a bit of blue')

# pprint
from pprint import pprint
x = {
    'A': { 'apple': [1, 2, 3], 'orange': [4, 5, 6, 7] },
    'B': { 'apple': [1, 2], 'orange': [4, 5, 6] },
    'C': { 'apple': [1, 2, 3, 4, 5], 'orange': [4, 5] }
}
pprint(x, indent=4)

# Entering password
from getpass import getpass
# your_pass = getpass()
# print(f"'{your_pass}'")


# Instaructions after Return
def fun():
    try:
        ...
        ...
        ...
        return 0
    except:
        print('Exception!!!')
    finally:
        print('After return instraction')
print(fun())

# Unprinting
from time import sleep
CURSOR_UP = '\033[1A'
CLEAR = '\x1b[2K'
CLEAR_LINE = CURSOR_UP + CLEAR
print('Witam!')
print('Witam!')
# sleep(1)
# print('Ty geju!')
# sleep(1)
# print(CLEAR_LINE, end='')
# print('Witam! ;)')

# Creating a class using type()
def init(self):
    print('Siema eniu!')
my_type = type('MyClass', (), {'__init__':init})
my_type()

# Open a browser
import webbrowser
# webbrowser.open('http://onet.pl')

# globals
globals()['x'] = 'global string'
print(x)

# Mapping proxies
print(my_type.__dict__, type(my_type.__dict__))