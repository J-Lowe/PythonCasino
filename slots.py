#  slots.py
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


from random import *
from blackjack import parseCommand

# Payment is based off 3 of any one symbol, with Wild being able to replace all symbols except Cherry
#	3 Wild		-- 100
#	3 Bell		-- 50
#	3 Orange	-- 15
#	3 Lemon		-- 10
#	3 Cherry	-- 7
#	2 Cherry	-- 5
#	1 Cherry	-- 1
def payment(wheels):
	if (wheels.count("Wild") == 3):
		return 100
	elif ((wheels.count("Wild") > 0 and wheels.count("Bell") == 2) or (wheels.count("Wild") == 2 and wheels.count("Bell")) or wheels.count("Bell") == 3):
		return 50
	elif ((wheels.count("Wild") >0 and wheels.count("Plum") == 2) or (wheels.count("Wild") == 2 and wheels.count("Plum")) or wheels.count("Plum") == 3):
		return 25
	elif ((wheels.count("Wild") > 0 and wheels.count("Orange") == 2) or (wheels.count("Wild") == 2 and wheels.count("Orange")) or wheels.count("Orange") == 3):
		return 15
	elif ((wheels.count("Wild") > 0 and wheels.count("Lemon") == 2) or (wheels.count("Wild") == 2 and wheels.count("Lemon")) or wheels.count("Lemon") == 3):
		return 10
	elif (wheels.count("Cherry") == 3):
		return 7
	elif (wheels.count("Cherry") == 2):
		return 5
	elif (wheels.count("Cherry") == 1):
		return 1
	else:
		return 0

# Tests "all"" combinations of payments
def testPayment():
	wheels = ["Wild", "Wild", "Wild"]
	print("3 Wild\tExpexted: 100\tTest: %d" % payment())
	wheels= ["Bell", "Bell", "Bell"]
	print("3 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Wild", "Bell", "Bell"]
	print("2 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Bell", "Wild", "Bell"]
	print("2 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Bell", "Bell", "Wild"]
	print("2 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Wild", "Wild", "Bell"]
	print("1 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Wild", "Bell", "Wild"]
	print("1 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Bell", "Wild", "Wild"]
	print("1 Bell\tExpexted: 50\tTest: %d" % payment())
	wheels= ["Plum", "Plum", "Plum"]
	print("3 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Wild", "Plum", "Plum"]
	print("2 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Plum", "Wild", "Plum"]
	print("2 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Plum", "Plum", "Wild"]
	print("2 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Wild", "Wild", "Plum"]
	print("1 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Wild", "Plum", "Wild"]
	print("1 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Plum", "Wild", "Wild"]
	print("1 Plum\tExpexted: 25\tTest: %d" % payment())
	wheels= ["Orange", "Orange", "Orange"]
	print("3 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Wild", "Orange", "Orange"]
	print("2 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Orange", "Wild", "Orange"]
	print("2 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Orange", "Orange", "Wild"]
	print("2 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Wild", "Wild", "Orange"]
	print("1 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Wild", "Orange", "Wild"]
	print("1 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Orange", "Wild", "Wild"]
	print("1 Orange\tExpexted: 15\tTest: %d" % payment())
	wheels= ["Lemon", "Lemon", "Lemon"]
	print("3 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Wild", "Lemon", "Lemon"]
	print("2 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Lemon", "Wild", "Lemon"]
	print("2 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Lemon", "Lemon", "Wild"]
	print("2 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Wild", "Wild", "Lemon"]
	print("1 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Wild", "Lemon", "Wild"]
	print("1 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Lemon", "Wild", "Wild"]
	print("1 Lemon\tExpexted: 10\tTest: %d" % payment())
	wheels= ["Cherry", "Cherry", "Cherry"]
	print("3 Cherry\tExpexted: 7\tTest: %d" % payment())
	wheels= ["Any", "Cherry", "Cherry"]
	print("2 Cherry\tExpexted: 5\tTest: %d" % payment())
	wheels= ["Cherry", "Any", "Cherry"]
	print("2 Cherry\tExpexted: 5\tTest: %d" % payment())
	wheels= ["Cherry", "Cherry", "Any"]
	print("2 Cherry\tExpexted: 5\tTest: %d" % payment())
	wheels= ["Any", "Any", "Cherry"]
	print("1 Cherry\tExpexted: 1\tTest: %d" % payment())
	wheels= ["Any", "Cherry", "Any"]
	print("1 Cherry\tExpexted: 1\tTest: %d" % payment())
	wheels= ["Cherry", "Any", "Any"]
	print("1 Cherry\tExpexted: 1\tTest: %d" % payment())
	wheels= ["Plum", "Bell", "Wild"]
	print("Junk\tExpexted: 0\tTest: %d" % payment())

# Play a game of slots with a starting sum of money!
def slots(money):
	items = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Wild']
	wheels = ["Dud", "Dud", "Dud"]
	startingMoney = money
	print("Welcome to my Python Slot Machine!")
	print("You'll pay $5 for each spin and earn money based on what appears on the spinners.")
	print("The payouts are as follows (Wild can replace any symbol besides Cherry):")
	print("\tWild\tWild\tWild\t=$100")
	print("\tBell\tBell\tBell\t=$50")
	print("\tPlum\tPlum\tPlum\t=$25")
	print("\tOrange\tOrange\tOrange\t=$15")
	print("\tLemon\tLemon\tLemon\t=$10")
	print("\tCherry\tCherry\tCherry\t=$7")
	print("\tCherry\tCherry\t-\t=$5")
	print("\tCherry\t-\t-\t=$1")
	command = "hihihihi"
	
	while(money > 4 and command != "no" and command != "n"):
		command = input("Would you like to spin for $5?\n> ")
		while (not parseCommand(command)):
			print("I'm sorry, I didn't understand that.")
			command = input("would you like to spin for $5?\n> ")
		if (command == "yes" or command == "y"):
			money -= 5
			wheels[0] = choice(items)
			wheels[1] = choice(items)
			wheels[2] = choice(items)
			print("%s\t%s\t%s" % (wheels[0], wheels[1], wheels[2]))
			payout = payment(wheels)
			if (payout > 0):
				print("You won $%d!" % payout)
			else:
				print("You lost . . .")
			money += payout
			print ("You currently have $%d" % money)
	
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
