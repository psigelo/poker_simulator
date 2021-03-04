from core.cards import cards
import copy
import random

def get_new_deck():
    deck = {"object_type": "deck", "cards_remain": [], "cards_gived": []}
    cards_new = copy.copy(cards)
    random.shuffle(cards_new)
    deck["cards_remain"]=cards_new

    return deck
