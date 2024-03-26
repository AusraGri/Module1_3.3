from CardDeck import CardDeck
from class_player import Player
import time


def main():
    player_1 = get_player_name(1)
    player_2 = get_player_name(2)
    gameplay(player_1, player_2)


def get_player_name(n):
    while True:
        try:
            name = input(f"Player {n} name: ")
            if not name:
                raise ValueError("Invalid name input")
            if len(name) > 50:
                raise ValueError("Invalid name. Please use shorter name")
            return name
        except ValueError:
            raise


def compare_cards(card1, card2):
    cards = []
    sep = f"{" - " * 20}"
    if card1.value > card2.value:
        print(sep)
        print(f"{card1} is higher than {card2}")
        print(sep)
        cards += [card1, card2]
        return 1
    elif card2.value > card1.value:
        print(sep)
        print(f"{card2} is higher than {card1}")
        print(sep)
        cards += [card1, card2]
        return 2
    else:
        print(sep)
        print(f"{card1} is equal to {card2}")
        print(sep)
        return 0


def gameplay(name_1, name_2):
    c = CardDeck()
    c.card_deck()
    c.deck_shuffle()
    p1_hand, p2_hand = c.card_split()
    player1 = Player(name_1, p1_hand)
    player2 = Player(name_2, p2_hand)
    cards = []
    while len(player1.hand) != 0 or len(player2.hand) != 0:
        print()
        time.sleep(1)
        print(f"+++ {name_1} +++ has {len(player1.hand)} cards")
        print(f"=== {name_2} === has {len(player2.hand)} cards")
        time.sleep(1)
        print()
        card1 = player1.lay_card()
        card2 = player2.lay_card()
        print(f"{name_1} making a move with -> {card1}")
        time.sleep(1)
        print(f"{name_2} stikes back with -> {card2}")
        time.sleep(1)
        result = compare_cards(card1, card2)
        if result == 1:
            cards += [card1, card2]
            player1.take_card(cards)
            print(f"+++ {name_1} wins this round! +++")
            print(" - " * 20)
            cards = []
        elif result == 2:
            cards += [card1, card2]
            player2.take_card(cards)
            print(f"=== {name_2} wins this round! ===")
            print(" - " * 20)
            cards = []
        else:
            cards += [card1, card2]
            hidden_card1 = player1.lay_card()
            hidden_card2 = player2.lay_card()
            print(f"{name_1} lays one hidden card")
            print(f"{name_2} lays one hidden card")
            cards += [hidden_card1, hidden_card2]

    if len(player1.hand) > len(player2.hand):
        print(f"Congratulations! The winner is {name_1}")
    else:
        print(f"Congratulations! The winner is {name_2}")


if __name__ == "__main__":
    main()
