import sys, os
from .functions import *
from .__main__ import sensors
from .__main__ import generate

menu_actions = {}
temp_list = []

def main_menu():
    os.system('clear')

    print(30 * '-')
    print('MAIN MENU')
    print(30 * '-')

    print('Welcome,\n')
    print('Please choose an option"')
    print('1. Record Temps')
    print('2. Print Recorded Temps')
    print('3. Print Current Temps')
    print('\n0. Quit')
    print(30 * '-')

    choice = input(">>  ")
    exec_menu(choice)

    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid Selection, please try again\n")
            menu_actions['main_menu']()
    return

# Record Menu
def record_menu():
    print("Record options:\n")
    print("3. Start recording.")
    print("9. Back")
    print("0. Quit")
    choice = input(">>  ")
    exec_menu(choice)
    return

def recording():
    print("Recording...")
    print("Press CTRL+C to stop recording.")
    record_temps(temp_list)
    print("Done recording.")
    print("4. Save and Quit.")
    print("9. Back.")
    print("0. Exit without saving.")
    choice = input(">>  ")
    exec_menu(choice)
    return


def print_recorded_temps():
    print("Recorded temps:\n")
    # record_temps()
    print("2. Print Again")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def back():
    menu_actions['main_menu']()

def save_and_quit():
    export_temp_csv('tempexport.csv', temp_list)
    print("Done!  Goodbye!")
    exit()

def exit():
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': record_menu,
    '2': print_recorded_temps,
    '3': recording,
    '4': save_and_quit,
    '9': back,
    '0': exit,
}