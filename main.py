import CardDeck

class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand


def main():
    c = CardDeck()
    c.card_deck()
    c.deck_shuffle()
    p1_hand, p2_hand = c.card_split()
    name = input("Enter player 1 name: ")
    player1 = Player(name, p1_hand)
    name = input("Enter player 2 name: ")
    player2 = Player(name, p2_hand)
    print("""
    Welcome to the War card game!
    """)


if __name__=="__main__":
    main()