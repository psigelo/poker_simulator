cards_value = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
card_to_number = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11,
                  'Q':12, 'K':13, 'A':14}
alternative_card_to_number = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11,
                              'Q':12, 'K':13, 'A':1}
cards_suit = {'pika', 'heart', 'diamond', 'clover'}
cards = [{"card_value": card_value, "card_suit": card_suit} for card_value in cards_value for card_suit in cards_suit]


def create_card(card_value: str, card_suit: str):
    return {'card_value': card_value, 'card_suit': card_suit}
