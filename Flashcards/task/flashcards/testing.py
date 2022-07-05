import random

cards = {
    "russia": 'moscow',
    "france": 'paris',
    "usa": 'washington',
}

card = random.choice(list(cards))

print(card)


#
# def __ask():
#     print('How many times to ask?How many times to ask?')
#     times = int(input())
#
#     for _ in range(times):
#         card = random.choice(cards)
#         print(f'Print the definition of "{card}":')
#         answer = input()
#         __check_definition(cards[card], answer)
#
# def __check_definition( definition, answer):
#     if answer == definition:
#         print('Correct')
#     elif answer in cards.values():
#         idx = list(cards.values()).index(answer)
#         print(f'Wrong. The right answer is "{definition}", '
#               'but your definition is correct for '
#               f'"{list(cards.keys())[idx]}".')
#     else:
#         print(f'Wrong. The right answer is "{definition}".')
#
# __ask()
#
#
#
