from random import shuffle

class Card:
    def __init__(self, sign, rank, value) -> None:
        self.sign = sign
        self.rank = rank
        self.value = value

    def __str__(self) -> str:
        return f"{self.rank}{self.sign}"


class CardDeck(Card):
    def __init__(self):  
        self.cardDeck = self.card_deck() 
        self.player_hands = ""
    
    def card_deck(self):
        signs = ["\u2664", "\u2661", "\u2662", "\u2667"]
        card_rank_value = {"A": 14, "K": 13, "Q": 12, "J": 11, 
                           "10": 10, "9": 9, "8": 8, "7": 7,
                            "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        card_deck = []
        for sign in signs:
            for rank in card_rank_value:
                card_deck.append(Card(sign, rank, card_rank_value[rank]))  
        return card_deck

    def __str__(self):
        return self.player_hands
    
    def deck_shuffle(self):
        shuffle(self.cardDeck)

    def card_split(self, number_of_players):
        if int(number_of_players)>0 and int(number_of_players)%2 == 0:
            players = int(number_of_players)
            hand_size = len(self.cardDeck) // players
            hands = []
            start = 0
            for _ in range(players):
                hand_end = start + hand_size 
                hands.append(self.cardDeck[start:hand_end])
                start = hand_end + 1
            # self.player_hands = hands
            return hands
        else:
            print("Error: Wrong number as parameter")

    
 
    def card_compare(self, card1, card2):
        pass


c = CardDeck()
hands = c.card_split(4)
player1 = hands[0]
player2 = hands[1]
print(len(player1))
print(len(player2))

# print(hands)
# for i, hand in enumerate(hands, start=1):
#     print(f"Player {i} cards:")
#     for card in hand:
#         print(card)
#     print() 