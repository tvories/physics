import sys
import datetime
from .menu import *
from .__init__ import *

options = ['menu', 'temp']


def get_all_temp():
        print('temps!')

def main():
    print('in main')

    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    # Run command based on options.  If command not found, print options.
    if len(args) > 0:
        if args[0].lower() == 'menu':
            if args[1].lower() == 'generate':
                generate = True
            main_menu()
        elif args[0].lower() == 'temp':
            get_all_temp()
    else:
        print('Please use one of the following commands:')
        for option in options:
            print('Option: {}'.format(option))

    if __name__ == '__main__':
        main()