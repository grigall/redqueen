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
	def __init__(self, name, desc, hand, hand_limit, coterie, actions, stats):
		self.name = name
		self.desc = desc
		self.hand = hand
		self.hand_limit = hand_limit
		self.coterie = coterie
		self.actions = actions
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

def enum_deck_short(deck):
	for i in range(0, len(deck)):
		print(f"{i+1}) ", deck[i].name, " of ", deck[i].suit)

#Shuffles the deck
def shuffle_deck(deck):
	import numpy as np
	shuffled_deck = list(np.random.permutation(deck))
	return shuffled_deck

#Generates player character and NPCs
def set_players():	
	player = Player(None, None, None, 6, [], 4, None)
	
	#Generate NPCs
	def npc_gen():
		npc_names = ['Jay-quellen', 'A\'Aron', 'Dee-Nice']
		npc_desc = ['Future business leader of America.', 'In the Glee Club.', 'That\'s not my name.']
		npc_list = []
	
		for i in range(0, len(npc_names)):
			npc = Player(npc_names[i], npc_desc[i], None, 5, [], 2, None)
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
			
	#enum_players(player_list) #shows list of players

def clear_screen():
	from os import system, name
	from time import sleep
	
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	
	sleep(0.05)

#Setup Game
def game_setup():
	#Sets global variables
	global deck, new_deck, player_list, turn
	#Initiates deck	
	deck = generate_deck()
	new_deck = shuffle_deck(deck)
	discard_pile = []

	#Initiates players
	player_list = set_players()
	
	#Initial Card Deal of the game
	deal_cards(new_deck)
	
	turn = 1

###
#This is the Starting Splash Screen 
###

def start_screen():
	print('\n')
	print("#####################")
	print("###   RED QUEEN   ###")
	print("#####################")
	print("\nWelcome to Red Queen: the game of tactical choices and strategic blunders!")
	print("\n")
	while True:
		start_menu = int(input("1) New Game\n2) Exit to Desktop\n"))
		if start_menu == 1:
			clear_screen()
			#Initiate Game
			game_setup() #Deal cards, initialize players, etc.
			player_list[-1].name = input("What is your name?\n")
			clear_screen()
			
			player_list[-1].desc = input("Please provide a brief description of yourself.\n")
			clear_screen()
			player_as_queen()
		else:
			break						
					

#Player turn function when playing as queen
def player_as_queen():
	print(f"\nHello {player_list[-1].name}! You have the following cards in your hand:")
	enum_deck_short(player_list[-1].hand)
	
	#Reset player available actions
	if turn == 1:
		player_list[-1].actions = 4
	else: 
		player_list[-1].actions = 3
	
	#List coterie
	if player_list[-1].coterie == None:
		print("\nYou have no cards in your coterie at the present.")
	else:
		print(f"\nYou have the following cards in your coterie:")
		enum_deck_short(player_list[-1].coterie)
	
	#Loop for player actions
	while player_list[-1].actions > 0:
		clear_screen()
		choice = int(input(f"You have {player_list[-1].actions} actions left. What would you like to do?\n\n1) Draw Card\n2) Play Card\n3) Shuffle Coterie\n4) View Hand\n5) View Coterie\n6) Discard\n7) Pass\n\nPick a number: "))
		#Draw Card
		if choice == 1:
			if len(player_list[-1].hand) < player_list[-1].hand_limit:
				clear_screen()
				player_list[-1].hand.append(new_deck[0])
				new_deck.pop(0)
				print(f"You\'ve drawn the {player_list[-1].hand[-1].name} of {player_list[-1].hand[-1].suit}.")
				player_list[-1].actions -= 1
				cont = input("\nPress ENTER to continue...")
			elif len(player_list[-1].hand) == player_list[-1].hand_limit:
				print(f"You have {len(player_list[-1].hand)} cards in your hand. You will have to discard if you have this number of cards at the end of your turn.")
				cont = input("\nPress ENTER to continue...")
		#Play Card
		elif choice == 2:
			if player_list[-1].coterie == None or len(player_list[-1].coterie) < 3:
				clear_screen()
				enum_deck_short(player_list[-1].hand[1:])
				coterie_choice = int(input("Which card would you like to add to your coterie?\n"))
				
				player_list[-1].coterie.append(player_list[-1].hand[coterie_choice])
				player_list[-1].hand.pop(coterie_choice)
				player_list[-1].actions -= 1
				cont = input("\nPress ENTER to continue...")
			else:
				print('Your coterie is full!')
				cont = input("\nPress ENTER to continue...")
		#Shuffle Coterie	
		elif choice == 3:
			if player_list[-1].coterie == None:
				print("Your coterie is empty!")
				cont = input("\nPress ENTER to continue...")
			else:
				clear_screen()
				shuffle_deck(player_list[-1].coterie)
				player_list[-1].actions -= 1
				enum_deck_short(player_list[-1].coterie)
				cont = input("\nPress ENTER to continue...") 
		#View Hand
		elif choice == 4:
			clear_screen()
			print("Your Hand:\n")
			enum_deck_short(player_list[-1].hand)
			cont = input("\nPress ENTER to continue...")
		#View Coterie
		elif choice == 5:
			clear_screen()
			if player_list[-1].coterie == None:
				print("Your coterie is empty!")
				cont = input("\nPress ENTER to continue...")
			else:
				print("Your Coterie:\n")
				enum_deck_short(player_list[-1].coterie)
				cont = input("\nPress ENTER to continue...")
		#Discard from Hand
		elif choice == 6:
			clear_screen()
			print("Your Hand:\n")
			enum_deck_short(player_list[-1].hand[1:])
			discard = input("\nWhich card would you like to discard?")
			player_list[-1].hand.pop(discard)
		#Pass
		else:
			break

def npc_turn():
	#Empty list for coterie matchup
	global battle_queue
	battle_queue = []
	
	#Iterate through NPCs
	for i in range(0, len(player_list - 1)):
		while player_list[i].actions > 0:
			#If NPC is playing as Red Queen
			if player_list[i].hand[0].card_id == 11:
				action = numpy.randint(1, 5)
				npc_action(action)
			#If NPC is playing as anyone else
			elif True:
				action = numpy.randint(0, 2)
				npc_action(action)

def battle_logic(attacker, defender):
	if len(defender.coterie) == 0:
		for i in range(0, len(battle_queue)):
			if battle_queue[i].kill_card == True:
				defeat_screen()
			else:
				break
	else:
		continue
		
	while len(battle_queue) > 0 and len(defender.coterie) > 0:
		for i in range(0, len(battle_queue)):
			#In case of matching face cards, attacker always wins
			if battle_queue[i].attack == defender.coterie[i].attack and battle_queue[i].face_card == True and defender.coterie[i].face_card == True:
				discard_pile.append(battle_queue[i])
				discard_pile.append(defender.coterie[i])
				battle_queue.pop(i)
				defender.coterie.pop(i)
				print(f"{battle_queue[i].name} beats {defender.coterie[i].name}!")
				sleep(1)
			#In case of same non-face cards
			elif battle_queue[i].attack == defender.coterie[i].attack and battle_queue[i].face_card == False and defender.coterie[i].face_card == False:
				attacker.hand.append(battle_queue[i])
				battle_queue.pop(i)
				print("Battle is a draw!")
				sleep(1)
			#Any other situation
			elif battle_queue[i].attack > defender.coterie[i].attack:
				discard_pile.append(battle_queue[i])
				discard_pile.append(defender.coterie[i])
				battle_queue.pop(i)
				defender.coterie.pop(i)
				print(f"{battle_queue[i].name} beats {defender.coterie[i].name}!")
				sleep(1)
												
def npc_action(action):			
	import numpy
	from time import sleep
	
	if action == 0: #Play Card
		battle_queue.append(player_list[i].hand[0])
		player_list[i].hand.pop(0)
		print(f"{player_list[i].name} has played a card!")
		sleep(1) #Pause for effect		
	elif action == 1: #Draw Card
		player_list[i].hand.append(new_deck[0])
		new_deck.pop(0)				
		print(f"{player_list[i].name} has drawn a card!")
		sleep(1)
		#Loop until player discards down to hand limit
		while len(player_list[i].hand) > player_list[i].hand_limit:
			discard_pile.append(player_list[i].hand[-1])
			player_list[i].hand.pop(-1)
	elif action == 2: #Fill Coterie
		if len(player_list[i].coterie) < 3 and len(player_list[i].hand) > 1:
			player_list[i].coterie.append(player_list[i].hand[1])
		else:
			print(f"{player_list[i].name}'s coterie is full!")
			sleep(1)								
	elif action == 3: #Shuffle Coterie
		shuffle_deck(player_list[i].coterie)
		print(f"{player_list[i].name} shuffled their coterie!")
		sleep(1)
	elif action == 4: #Pass
		print(f"{player_list[i].name} chose to pass.")
		sleep(1)											

def defeat_screen():
	from time import sleep
	print("You have been defeated.")
	sleep(0)						

###################
###  Starts the Game  ###
###################
start_screen()				