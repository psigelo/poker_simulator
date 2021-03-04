from core.cards import cards
import copy
import random


class Deck(object):
    def __init__(self):
        self.deck = None
        self.create_new_deck()

    def create_new_deck(self):
        self.deck = {"object_type": "deck", "cards_remain": [], "cards_gived": []}
        cards_new = copy.copy(cards)
        random.shuffle(cards_new)
        self.deck["cards_remain"]=cards_new


    def get_next_card(self)->dict:
        if len(self.deck["cards_remain"])==0:
            return {}
        
        new_card = self.deck["cards_remain"].pop()
        self.deck["cards_gived"].append(new_card)
        return new_card
