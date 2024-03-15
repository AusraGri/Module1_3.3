from CardDeck import CardDeck

class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def lay_card(self):
        card = self.hand[0]
        self.hand.remove(self.hand[0])
        return card
    
    def take_card(self, cards):
        for card in cards:
            self.hand.append(card)


def main():
    c = CardDeck()
    c.card_deck()
    c.deck_shuffle()
    p1_hand, p2_hand = c.card_split()
    name = "DAVE"
    player1 = Player(name, p1_hand)
    name2 = "BOB"
    player2 = Player(name2, p2_hand)
    card1 = player1.lay_card()
    card2 = player2.lay_card()
    compare_cards(card1.value, card2.value)

    
    
def compare_cards(card1, card2):
    if card1 > card2:
        print(f"{card1} higher than {card2}")
    elif card2 > card1:
        print(f"{card2} higher than {card1}")
    else:
        print(f"{card1} equal {card2}")




if __name__=="__main__":
    main()