from itertools import combinations
from core.cards import card_to_number, alternative_card_to_number
import pandas as pd

HAND_SIZE = 5
poker_hands = {"high_card":1, "pair":2, "two_pairs":3,
        "tree_of_a_kind":4, "straight":5, "flush":6, "four_of_a_kind":7, 
        "straight_flush":8, "royal_flush":9}


def sort_card_key(card):
    return card_to_number[card["card_value"]]


def sort_hand(cards):
    cards.sort(key=sort_card_key)


def check_royal_flush(all_hands_combinations):
    for hand in all_hands_combinations:
        hand.sort(key=sord_card_key)


### ==== STRAIGHT FUNCTIONS ZONE ====

def get_better_straight(all_straight_hands):
    all_straight_hands.sort(key=lambda x: x['high'], reverse=True)
    return all_straight_hands[0]

def get_straight_if_exist(all_combinations):
    all_straight_hands = list()
    
    for hand5 in all_hands_combinations:
        hand5.sort(key=sort_card_key)
        hand5_df = pd.DataFrame(hand)
        hand5_df["card_number_value"] = hand7_df["card_value"].apply(lambda x: card_to_number[x])
        hand5_df["alternative_card_number_value"] = hand7_df["card_value"].apply(lambda x: alternative_card_to_number[x]) 

        # other cases
        if hand5_df['card_number_value'].diff().sum() == 4:
            all_straight_hands.append({'hand': hand5, 'hand_type': 'straight', 'high': hand5.card_number_value.max()})
        else:
            if hand5_df['alternative_card_number_value'].diff().sum() == 4:
                # Case Ace,2,3,4,5
                all_straight_hands.append('hand': hand5, 'hand_type': 'straight', 'high': 5})

    if len(all_straight_hands) == 0:
        return None
    elif len(all_straight_hands) == 1:
        return all_straight_hands[0]
    else:
        return get_better_straight(all_straight_hands)

###  ==== STRAIGHT FUNTIONS ZONE END ====




def getting_better_hand(card_list):
    # getting better 5 cards of 7 cards available.
    all_combinations = combinations(card_list, HAND_SIZE)
    
    # first check if rotal_flush
    
        
