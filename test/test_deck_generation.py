from core.deck import Deck
deck = Deck()
print(deck.deck)
for it in range(54):
    print(deck.get_next_card())

print(deck.deck)
