#  blackjack.py
#  
#  Copyright 2017 Jonathan Lowe <jonathanlowe01@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from card import *
from deck import *

def parseCommand(command):
	return command == "yes" or command == "no" or command == "y" or command == "n"

# Start a game of Blackjack with a starting wallet size
def blackjack(money):
	startingMoney = money
	print("Welcome to my Python Blackjack Game!")
	print("Each round you'll play against a semi-competent dealer.")
	print("Answer each prompt with 'yes' or 'no' only.")
	print("Hope you enjoy!")
	print()
	print()
	print()

	command = "yes"
	
	# Go until the user runs out of money or they don't want to play again
	while (money > 0 and (command == "yes" or command == "y")):
		deck = Deck()
		player = Hand()
		dealer = Hand()
		deck.shuffle()
		command = input("Want to bet $5 to start a new round?\n> ")
		# Check for valid input
		while (not parseCommand(command)):
			print("I'm sorry, I didn't understand that.")
			command = input("Want to bet $5 to start a new round?\n> ")
		# User wants to play another round
		if (command == "yes" or command == "y"):
			money -= 5 # Bet $5
			dealer.addCard(deck.draw())
			player.addCard(deck.draw())
			dealer.addCard(deck.draw())
			# While the user wants to "get hit" (or just started the round)
			while (command == "yes" or command == "y"):
				player.addCard(deck.draw())
				print("Dealer's hand: %s (%d)" % (dealer, dealer.getValue()))
				print ("Your hand: %s (%d)" % (player, player.getValue()))
				# Make sure the player hasn't busted and/or hit Blackjack
				if (player.getValue() < 21):
					command = input("Would you like another card?\n> ")
					while (not parseCommand(command)):
						print("I'm sorry, I didn't understand that.")
						command = input("Would you like another card?\n> ")
				# Bother busting and hitting Blackjack means no more hitting
				elif (player.getValue() >= 21):
					command = "no"
			# Player has stopped getting cards
			# If they have 21, they win, so no need to deal any cards to "AI"
			if (player.getValue() < 21):
				while (dealer.getValue() < player.getValue()):
					dealer.addCard(deck.draw())
				print("Dealer's hand: %s (%d)" % (dealer, dealer.getValue()))
				print ("Your hand: %s (%d)" % (player, player.getValue()))
			# Player only wins if they:
			#		- Have more points than the dealer and haven't busted
			#		- The dealer busted
			# Yes, this means a tie favors the Casino.  Deal with it.
			if (player.getValue() > dealer.getValue() and player.getValue() <= 21 or dealer.getValue() > 21):
				print("Congrats!  You won this round.")
				money += 10
			else:
				print("Oh no!  You lost this round.")
			print("New balance: $%d" % money)
			command = "yes" # Makes sure the user is prompted to start a new round
	# Calculates total profit/loss
	profit = ""
	p = money - startingMoney
	if (p > 0):
		profit = "profit of $%d" % p
	else:
		p = -p
		profit = "loss of $%d" % p
	# A nice message to inform the player of how well/poorly they did before returning to the rest
	# of the casino
	print("You ended up with $%d, for a total %s.  Hope to see you again!" % (money, profit))
	return money
