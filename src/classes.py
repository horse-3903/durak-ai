from __future__ import annotations

import random
from collections import Counter

suit_lst = ["Clubs", "Hearts", "Spades", "Diamonds"]
sym_lst = ["♣", "♥", "♠", "♦"]
face_lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
check_lst = ["Nothing", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]

class Card:
    def __init__(self, suit: str, face: str) -> None:
        if suit not in suit_lst:
            raise ValueError("Suit not valid")
        
        if face not in face_lst:
            raise ValueError("Face not valid")
        
        self.suit = suit
        self.symbol = sym_lst[suit_lst.index(suit)]
        self.face = face
        self.value = face_lst.index(face) + 2

    def __gt__(self, other: Card) -> bool:
        if self.value != other.value:
            return self.value > other.value
        
        return suit_lst.index(self.suit) > suit_lst.index(other.suit)
    
    def __lt__(self, other: Card) -> bool:
        if self.value != other.value:
            return self.value < other.value
        
        return suit_lst.index(self.suit) < suit_lst.index(other.suit)
    
    def __str__(self) -> str:
        return f"{self.face} {self.symbol}"
    
    def __repr__(self) -> str:
        return f"{self.face} {self.symbol}"
        
class Card_Set:
    def __init__(self, card_set: list = []) -> None:
        self.set = card_set
        
    def add_card(self, card: Card) -> None:
        assert isinstance(card, Card)
        
        self.set.append(card)

    def sort_set(self) -> None:
        self.set = sorted(self.set)

    def check_set(self) -> tuple[int, int]:
        self.sort_set()

        res_code = 0

        val = [c.value for c in self.set]
        face = [c.face for c in self.set]

        # checks for same suit
        if all(self.set[0].suit == c.suit for c in self.set):
            cmp = [*range(min(self.set).value, max(self.set).value+1)]
            
            if val != cmp:
                res_code = max(res_code, 5) # flush
            else:
                res_code = max(res_code, 8) # straight flush
        
        # different suit
        else:
            face_counter = Counter(face).most_common()
            
            most_common = face_counter[0]
            sec_common = face_counter[1]
            
            match most_common[1]:
                case 4:
                    res_code = max(res_code, 7) # four of a kind
                case 3:
                    # checks for full house
                    if sec_common[1] == 2:
                        res_code = max(res_code, 6) # full house
                    else:
                        res_code = max(res_code, 3) # three of a kind
                case 2:
                    # checks for two pair
                    if sec_common[1] == 2:
                        res_code = max(res_code, 2) # two pair
                    else:
                        res_code = max(res_code, 1) # one pair

            # check for straight
            if val == [*range(min(val), max(val)+1)]:
                res_code = max(res_code, 4)
        
        return (res_code, sum(val))

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(suit, face) for suit in suit_lst for face in face_lst]
        self.shuffle()
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def deal(self, num_cards: int) -> list[Card]:
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck")
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
    
    def __repr__(self) -> str:
        return f"Deck({len(self.cards)} cards remaining)"
    
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Card_Set()
        self.current_bet = 0

    def receive_cards(self, cards: list[Card]) -> None:
        for card in cards:
            self.hand.add_card(card)

    def __repr__(self) -> str:
        return f"Player({self.name}, Hand: {self.hand.set})"

class Game:
    def __init__(self, player_names: list[str]) -> None:
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
    
    def deal_cards(self, num_cards: int = 5) -> None:
        for player in self.players:
            player.receive_cards(self.deck.deal(num_cards))
    
    def determine_winner(self) -> Player:
        best_hand = None
        winner = None
        for player in self.players:
            hand_rank, hand_value = player.hand.check_set()
            if best_hand is None or hand_rank > best_hand[0] or (hand_rank == best_hand[0] and hand_value > best_hand[1]):
                best_hand = (hand_rank, hand_value)
                winner = player
        return winner
    
    def play(self) -> None:
        self.deal_cards()
        for player in self.players:
            print(f"{player.name}'s hand: {player.hand.set}")
        winner = self.determine_winner()
        print(f"The winner is {winner.name} with hand {winner.hand.set}")
