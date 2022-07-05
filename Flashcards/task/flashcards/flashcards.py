import sys
import os.path
import random


class FlashCards:
    __all_cards = dict()

    @classmethod
    def __get_term(cls):
        print('The card:')
        while True:
            term = input()
            if term not in cls.__all_cards.keys():
                return term
            print(f'The term "{term}" already exists. Try again:')

    @classmethod
    def __get_definition(cls):
        print('The definition of the card:')
        while True:
            definition = input()
            if definition not in cls.__all_cards.values():
                return definition
            print(f'The definition "{definition}" already exists. Try again:')


    @classmethod
    def display_menu(cls):
        print('Input the action (add, remove, import, export, ask, exit):')
        action = input()

        if action == 'add':
            cls.__add()
        if action == 'remove':
            cls.__remove()
        if action == 'import':
            cls.__import()
        if action == 'export':
            cls.__export()
        if action == 'ask':
            cls.__ask()
        if action == 'exit':
            cls.__exit()


    @classmethod
    def __add(cls):
        term = cls.__get_term()
        definition = cls.__get_definition()

        cls.__all_cards[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.')

    @classmethod
    def __remove(cls):
        print('Which card?')
        card_to_remove = input()

        if card_to_remove in cls.__all_cards:
            del cls.__all_cards[card_to_remove]
            print('The card has been removed.')
        else:
            print(f'Can\'t remove "{card_to_remove}": there is no such card.')

    @classmethod
    def __import(cls):
        print('File name:')
        file_name = input()

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                words = 0

                for line in file:
                    key, val = line.split()
                    cls.__all_cards[key] = val
                    words += 1

                print(f"{words} cards have been loaded.")
        else:
            print('File not found.')

    @classmethod
    def __export(cls):
        print('File name:')
        file_name = input()

        with open(f'{file_name}', 'w') as file:
            for val, key in cls.__all_cards.items():
                file.write(f"{val} {key}\n")

        print(f'{len(cls.__all_cards)} cards have been saved.')


    @classmethod
    def __ask(cls):
        print('How many times to ask?How many times to ask?')
        times = int(input())

        for _ in range(times):
            card = random.choice(list(cls.__all_cards))
            print(f'Print the definition of "{card}":')
            answer = input()
            cls.__check_definition(cls.__all_cards[card], answer)

    @classmethod
    def __check_definition(cls, definition, answer):
        if answer == definition:
            print('Correct')
        elif answer in cls.__all_cards.values():
            idx = list(cls.__all_cards.values()).index(answer)
            print(f'Wrong. The right answer is "{definition}", '
                  'but your definition is correct for '
                  f'"{list(cls.__all_cards.keys())[idx]}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')


    @classmethod
    def __exit(cls):
        print('Bye bye!')
        sys.exit()

while True:
    FlashCards.display_menu()
