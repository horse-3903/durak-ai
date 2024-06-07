from classes import *

test_cases = {
    "Nothing": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "4"),
        Card("Spades", "6"),
        Card("Diamonds", "8"),
        Card("Hearts", "10"),
    ]),
    "One Pair": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "2"),
        Card("Spades", "6"),
        Card("Diamonds", "8"),
        Card("Hearts", "10"),
    ]),
    "Two Pairs": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "2"),
        Card("Spades", "6"),
        Card("Diamonds", "6"),
        Card("Hearts", "10"),
    ]),
    "Three of a Kind": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "2"),
        Card("Spades", "2"),
        Card("Diamonds", "8"),
        Card("Hearts", "10"),
    ]),
    "Straight": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "3"),
        Card("Spades", "4"),
        Card("Diamonds", "5"),
        Card("Hearts", "6"),
    ]),
    "Flush": Card_Set([
        Card("Hearts", "2"),
        Card("Hearts", "4"),
        Card("Hearts", "6"),
        Card("Hearts", "8"),
        Card("Hearts", "10"),
    ]),
    "Full House": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "2"),
        Card("Spades", "2"),
        Card("Diamonds", "6"),
        Card("Hearts", "6"),
    ]),
    "Four of a Kind": Card_Set([
        Card("Hearts", "2"),
        Card("Clubs", "2"),
        Card("Spades", "2"),
        Card("Diamonds", "2"),
        Card("Hearts", "10"),
    ]),
    "Straight Flush": Card_Set([
        Card("Hearts", "2"),
        Card("Hearts", "3"),
        Card("Hearts", "4"),
        Card("Hearts", "5"),
        Card("Hearts", "6"),
    ]),
}

for test_name, card_set in test_cases.items():
    res = card_set.check_set()
    print(f"{test_name}: {res}")
    print(test_name == check_lst[res[0]])