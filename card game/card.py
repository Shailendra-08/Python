
# Deck

# Dictionay value of Deck in key value player

import random

suits = ('Hearts', 'Diamonds','Spades','Clubs')
ranks =('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values= {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
         'Jack':11,'Queen':12,'King':13,'Ace':14}


#Card,Suit and rank value
class Card:
    def __init__(self,suit,rank):
        self.suit =suit
        self.rank =rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    #all 52 cards in the box
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create a Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    #shuffle all 52 card using random.shuffle
    def shuffle(self):
        random.shuffle(self.all_cards)

    #After shuffle delete one card from the deck
    def deal_one(self):
        return self.all_cards.pop()


# new_deck= Deck()
# new_deck.shuffle()
# my_card = new_deck.deal_one()
# print(my_card)

# print(len(my_card))
# first_card = new_deck.all_cards[0]
# bottom_card = new_deck.all_cards[-1]

# print(first_card)
# print(bottom_card)
#
# new_deck.shuffle()
# bottom_card = new_deck.all_cards[-1]
# print(bottom_card)



# for card_obj in new_deck.all_cards:
#     print(card_obj)



class Player:

    def __init__(self,name):
        self.name =name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([ ]):
            #List of multiple Card Object
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# new_player = Player('Ayush')
# print(new_player)
# print(new_player.add_cards(my_card))
# print(new_player)



# Game Setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()


# Split the deck between the two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


#While game_on

game_on = True
round_num = 0

# while game_on:
#     round_num += 1
#     print(f"Round {round_num}")
#
#     if len(player_one.all_cards) == 0:
#         print("Player One is out of cards!!!")
#         print("Player Two Win's the game")
#         game_on = False
#         break
#
#     if len(player_two.all_cards) == 0:
#         print("Player Two is out of cards!!!")
#         print("Player One Win's the game")
#         game_on = False
#         break
#
#     # Start a New Rounds
#     player_one_cards =[player_one.remove_one()]
#     player_two_cards =[player_two.remove_one()]
#
#     # while at_war
#     at_war= True
#     while at_war:
#         if player_one_cards[-1].value > player_two_cards[-1].value:
#             player_one.add_cards(player_one_cards)
#             player_one.add_cards(player_two_cards)
#             at_war = False
#
#         elif player_one_cards[-1].value < player_two_cards[-1].value:
#             player_two.add_cards(player_one_cards)
#             player_two.add_cards(player_two_cards)
#             at_war = False
#
#         else:
#             print("!!!  WAR   !!!")
#
#             if len(player_one.all_cards) < 5:
#                 print("Player One unable to declare war")
#                 print("Players two win's")
#                 game_on = False
#                 break
#             elif len(player_two.all_cards) < 5:
#                 print("Player Two unable to declare war")
#                 print("Players One win's")
#                 game_on = False
#                 break
#             else:
#                 for num in range(5):
#                     player_one.all_cards.append(player_one.remove_one())
#                     player_two.all_cards.append(player_two.remove_one())

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One is out of cards!!!")
        print("Player Two Wins the game")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards!!!")
        print("Player One Wins the game")
        game_on = False
        break

    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("!!! WAR !!!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player Two Wins")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One Wins")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())








