#Custom Class for card objects
class Card:
	def __init__(self, name, attack, suit, kill_card, face_card, card_id):
		self.name = name
		self.attack = attack
		self.suit = suit
		self.kill_card = kill_card
		self.face_card = face_card
		self.card_id = card_id

class Player:
	def __init__(self, name, desc, hand, stats):
		self.name = name
		self.desc = desc
		self.hand = hand
		self.stats = stats

#Function to generate full deck of cards
def generate_deck():
	#List of card names for regular suits
	card_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
	
	suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
	
	#Predefines the two joker cards
	joker_red = Card('Red Joker', 14, None, True, True, None)
	joker_black = Card('Black Joker', 14, None, True, True, None)
	
	#Empty list to dump generated cards into
	card_list = []
	
	#Function to automate card generation
	def card_gen(suit):
		for i in range(0, len(card_names)):
			card = Card(card_names[i], (i+2), suit, False, False, None)
			card_list.append(card)
	
	#Generates all four suits
	for i in range(0, len(suit_list)):
		card_gen(suit_list[i])
	
	#Identifies Face Cards
	for i in range(0, len(card_list)):
		if card_list[i].name in card_names[9:13]:
			card_list[i].face_card = True
		else:
			continue
	
	#Adds two jokers
	card_list.append(joker_red)
	card_list.append(joker_black)
	
	#Modifies kill properties of Jack of Hearts and Queen of Diamonds
	card_list[9].kill_card = True #Jack of Hearts
	card_list[23].kill_card = True #Queen of Diamonds
	
	#Set unique card id to index plus one
	for i in range(0, len(card_list)):
		card_list[i].card_id = i+1

	return card_list #Final "deck"
		
#Outputs Card List
def enum_deck(deck):
	for i in range(0, len(deck)):
		print(f"Name: ", deck[i].name, " of ", deck[i].suit)  
		print(f"Attack: ", deck[i].attack)
		print(f"Kill Card: ", deck[i].kill_card)
		print(f"Face Card: ", deck[i].face_card)
		print(f"Card ID: ", deck[i].card_id)
		print("")

#Shuffles the deck
def shuffle_deck(deck):
	import numpy as np
	shuffled_deck = list(np.random.permutation(deck))
	return shuffled_deck

#Generates player character and NPCs
player_name = None #input("What is your name?")
player_desc = None #input("Please provide a brief description of yourself.")

def set_players():	
	player = Player(player_name, player_desc, None, None)
	
	#Generate NPCs
	def npc_gen():
		npc_names = ['Jay-quellen', 'A\'Aron', 'Dee-Nice']
		npc_desc = ['Future business leader of America.', 'In the Glee Club.', 'That\'s not my name.']
		npc_list = []
	
		for i in range(0, len(npc_names)):
			npc = Player(npc_names[i], npc_desc[i], None, None)
			npc_list.append(npc)
	
		import numpy
		new_npc_list = list(numpy.random.permutation(npc_list))
		return new_npc_list
		
	player_list = npc_gen()
	player_list.append(player)
	return player_list

def enum_players(player_list):
	for i in range(0, len(player_list)):
		print(f"Name: ", player_list[i].name)
		print(f"Description: ", player_list[i].desc)
		enum_deck(player_list[i].hand)

#Initiates deck	
deck = generate_deck()
new_deck = shuffle_deck(deck)

#Initiates players
player_list = set_players()

#Function to deal cards
def deal_cards(new_deck):
	#Empty lists for player hand
	hand_player = []
	
	#Find the Red Queen
	for i in range(0, len(new_deck)):
		if new_deck[i].card_id == 11:
			hand_player.append(new_deck[i])
			new_deck.pop(i)
			break
		else:
			continue
	
	#Draw three more cards for Player
	for i in range(0, 3):
		hand_player.append(new_deck[i])
		new_deck.pop(i)
	
	#Draw cards for NPCs
	def npc_draw():
		hand_npc = []
		for i in range(0, 4):
			hand_npc.append(new_deck[i])
			new_deck.pop(i)
		return hand_npc
	
	#Place cards in hands
	for i in range(0,3):
		player_list[i].hand = npc_draw()
		
	#Place player's cards in hand
	player_list[-1].hand = hand_player
			
	enum_players(player_list)

deal_cards(new_deck)