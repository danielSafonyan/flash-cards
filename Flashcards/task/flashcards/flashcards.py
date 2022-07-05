class Cards:
    __num_cards = 0
    __all_cards = []
    all_terms = []
    all_defs = []

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

        Cards.__all_cards.append(self)
        Cards.all_terms.append(term)
        Cards.all_defs.append(definition)

    @classmethod
    def __get_term(cls):
        while True:
            term = input()
            if term not in cls.all_terms:
                return term
            print(f'The term "{term}" already exists. Try again:')

    @classmethod
    def __get_def(cls):
        while True:
            definition = input()
            if definition not in cls.all_defs:
                return definition
            print(f'The definition "{definition}" already exists. Try again:')


    @classmethod
    def __get_num_cards(cls):
        print('Input the number of cards:')
        cls.__num_cards = int(input())

    @classmethod
    def create_cards(cls):
        cls.__get_num_cards()
        for i in range(1, cls.__num_cards + 1):
            print(f'The term for card #{i}:')
            term = cls.__get_term()
            print(f'The definition for card #{i}:')
            definition = cls.__get_def()

            Cards(term, definition)

    @classmethod
    def check_definition(cls, term, definition, answer):
        if answer == definition:
            print('Correct')
        elif answer in cls.all_defs:
            idx = cls.all_defs.index(answer)

            print(f'Wrong. The right answer is "{definition}", '
                  'but your definition is correct for '
                  f'"{cls.all_terms[idx]}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')


    @classmethod
    def check_knowledge(cls):
        for card in cls.__all_cards:
            print(f'Print the definition of "{card.term}":')
            answer = input()
            cls.check_definition(card.term, card.definition, answer)


Cards.create_cards()
Cards.check_knowledge()

