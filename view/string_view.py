from core.cards import create_card

suit_2_string_suit = {"pika": 'p', 'heart': 'h', 'diamond': 'd', 'clover':'c'}
string_suit_2_suit = {'p': 'pika', 'h': 'heart', 'd': 'diamond', 'c': 'clover'}

def string_encode(cards: list) -> str:
    result_string = str()
    for card in cards:
        result_string += card["card_value"] + suit_2_string_suit[card['card_suit']]
    return result_string


def string_decode(string_cards: str) -> list:
    string_length = len(string_cards)
    result_cards = list()
    print(string_length)
    for it in range(int(string_length/2)):
        new_card = create_card(string_cards[2*it], string_suit_2_suit[string_cards[2*it +1]])
        result_cards.append(new_card)
    return result_cards

