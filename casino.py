#  casino.py
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


from blackjack import *
from slots import *

print("Welcome to Jalo's Casino.")
input()
print("We don't have very many games at the moment, but we are happy to offer games of Blackjack")
print("to anyone who wishes to play.")
input()
print("To play Blackjack, you'll start with $100 and will bet $5 per round until you decide to walk")
print("away.  Your only opponent will be our semi-competent dealer.")
input()
print("We hope you have a great time!")
input()

choice = "hihihihihi" # User's game selection
money = 100 # User's wallet
selectString = "\nWhich game would you like to play?\n1. Blackjack\n2. Slots\n3. Quit\n> " # Used in input()
choices = ["1", "2", "3"]
quitString = choices[-1] # Always the last option, will change as more options are added

# Go until the user selects the quit string or they run out of money
while(choice != quitString and money > 4):
	choice = input(selectString)
	# As the option list grows, I'll need to find a better way to check for valid input
	while(choice not in choices):
		print("I'm sorry, I didn't understand your response")
		choice = input(selectString)
	if(choice == "1"):
		money = blackjack(money)
	elif(choice == "2"):
		money = slots(money)

# Calculate total day's profit/loss
profit = ""
p = money - 100
if (p > 0):
	profit = "profit of $%d" % p
else:
	p = -p
	profit = "loss of $%d" % p

# Tell the user how well/poorly they did before quitting
print("It was nice doing business with you.")
print("You end the day with $%d, for a total %s." % (money, profit))
print("We hope you'll visit us again!")
