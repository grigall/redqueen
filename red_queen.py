#Custom Class for card objects
class Card:
	def __init__(self, name, attack, suit, kill_card, card_id):
		self.name = name
		self.attack = attack
		self.suit = suit
		self.kill_card = kill_card
		self.card_id = card_id
	
#List of card names for regular suits
card_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

#Predefines the two joker cards
joker_red = Card('Red Joker', 14, None, True, None)
joker_black = Card('Black Joker', 14, None, True, None)

#Empty list to dump generated cards into
card_list = []

#Function to automate card generation
def card_gen(suit):
	for i in range(0, len(card_names)):
		card = Card(card_names[i], (i+2), suit, False, None)
		card_list.append(card)

#Generates all four suits
for i in range(0, len(suit_list)):
	card_gen(suit_list[i])

#Adds two jokers
card_list.append(joker_red)
card_list.append(joker_black)

#Modifies kill properties of Jack of Hearts and Queen of Diamonds
card_list[9].kill_card = True #Jack of Hearts
card_list[23].kill_card = True #Queen of Diamonds

#Set unique card id to index plus one
for i in range(0, len(card_list)):
	card_list[i].card_id = i+1


for i in range(0, len(card_list)):
	print(f"Index Number: {i}")
	print(card_list[i].name)
	print(card_list[i].suit)
	print(card_list[i].attack)
	print(card_list[i].kill_card)
	print(card_list[i].card_id)
	print("")