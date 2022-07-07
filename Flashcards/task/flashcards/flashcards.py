import sys
import os.path
import random


class FlashCards:
    __all_cards = dict()
    __logs = []
    __num_errors = 0
    __error_words = []

    @classmethod
    def __get_term(cls):
        print('The card:')
        cls.__logs.append('The card:')
        while True:
            term = input()
            if term not in cls.__all_cards.keys():
                return term
            print(f'The term "{term}" already exists. Try again:')
            cls.__logs.append(f'The term "{term}" already exists. Try again:')
    @classmethod
    def __get_definition(cls):
        print('The definition of the card:')
        cls.__logs.append('The definition of the card:')
        while True:
            definition = input()
            if definition not in cls.__all_cards.values():
                return definition
            print(f'The definition "{definition}" already exists. Try again:')
            cls.__logs.append('The card:')

    @classmethod
    def display_menu(cls):
        message = 'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):'
        print(message)
        cls.__logs.append(message)
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
        if action == 'log':
            cls.__log()
        if action == 'hardest card':
            cls.__hardest_card()
        if action == 'reset stats':
            cls.__reset_stats()

    @classmethod
    def __reset_stats(cls):
        __num_errors = 0
        __error_words = []
        message = 'Card statistics have been reset.'
        print(message)
        cls.__logs.append(message)

    @classmethod
    def __log(cls):
        print('File name:')
        cls.__logs.append('File name:')
        file_name = input()
        with open(file_name, 'w') as logs:
            for line in cls.__logs:
                logs.write(f'{line}\n')
        print('The log has been saved.')

    @classmethod
    def __hardest_card(cls):
        if cls.__error_words:
            if len(cls.__error_words) == 1:
                message = f'The hardest card is "{cls.__error_words[0]}". You have {cls.__num_errors} errors answering it.'
            else:
                message = 'The hardest cards are '
                for idx, word in enumerate(cls.__error_words):
                    message += f'"{word}"'
                    if idx == len(cls.__error_words) - 1:
                        message += '. '
                    else:
                        message += ', '
                message += f'You have {cls.__num_errors} errors answering them.'
                print(message)
                cls.__logs.append(message)
        else:
            message = 'There are no cards with errors.'
            print(message)
            cls.__logs.append(message)
        print()


    @classmethod
    def __add(cls):
        term = cls.__get_term()
        definition = cls.__get_definition()

        cls.__all_cards[term] = definition
        message = f'The pair ("{term}":"{definition}") has been added.'
        print(message)
        cls.__logs.append(message)

    @classmethod
    def __remove(cls):
        print('Which card?')
        cls.__logs.append('Which card?')
        card_to_remove = input()

        if card_to_remove in cls.__all_cards:
            del cls.__all_cards[card_to_remove]
            message = 'The card has been removed.'
        else:
            message = f'Can\'t remove "{card_to_remove}": there is no such card.'
        print(message)
        cls.__logs.append(message)

    @classmethod
    def __import(cls):
        print('File name:')
        cls.__logs.append('File name:')
        file_name = input()

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                words = 0

                for line in file:
                    key, val = line.split()
                    cls.__all_cards[key] = val
                    words += 1

                message = f"{words} cards have been loaded."
        else:
            message = 'File not found.'

        print(message)
        cls.__logs.append(message)



    @classmethod
    def __export(cls):
        print('File name:')
        cls.__logs.append('File name:')
        file_name = input()

        with open(f'{file_name}', 'w') as file:
            for val, key in cls.__all_cards.items():
                file.write(f"{val} {key}\n")

        message = f'{len(cls.__all_cards)} cards have been saved.'

        print(message)
        cls.__logs.append(message)


    @classmethod
    def __ask(cls):
        message = 'How many times to ask?How many times to ask?'
        print(message)
        cls.__logs.append('File name:')
        times = int(input())

        for _ in range(times):
            card = random.choice(list(cls.__all_cards))
            print(f'Print the definition of "{card}":')
            cls.__logs.append(f'Print the definition of "{card}":')
            answer = input()
            if not cls.__check_definition(cls.__all_cards[card], answer):
                if card not in cls.__error_words:
                    cls.__error_words.append(card)
                cls.__num_errors += 1
            print()

    @classmethod
    def __check_definition(cls, definition, answer):
        if answer == definition:
            print('Correct')
            cls.__logs.append('Correct')
            return True
        elif answer in cls.__all_cards.values():
            idx = list(cls.__all_cards.values()).index(answer)
            message = f'Wrong. The right answer is "{definition}" ' \
                      f'but your definition is correct ' \
                      f'for {list(cls.__all_cards.keys())[idx]}".'
            print(message)
            cls.__logs.append(message)
            return False
        else:
            message = f'Wrong. The right answer is "{definition}".'
            print(message)
            cls.__logs.append(message)
            return False


    @classmethod
    def __exit(cls):
        print('Bye bye!')
        sys.exit()

while True:
    FlashCards.display_menu()
