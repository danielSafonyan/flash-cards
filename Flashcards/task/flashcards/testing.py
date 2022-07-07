error_words = ["Russia", "France"]
num_errors = 1


def hardest_card():
    if error_words:
        print(len(error_words))
        message = 'The hardest cards are '
        for idx, word in enumerate(error_words):
            print(idx, word)
            message += f"{word}"
            if idx == len(error_words):
                message += '. '
            else:
                message += ', '
        message += f'You have {num_errors} errors answering them.'
        print(message)

hardest_card()