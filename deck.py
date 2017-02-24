#  deck.py
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
from card import *

class Deck:
	'Defines properties of a standard playing card deck'
	
	def __init__(self):
		self.cardList = []
		for suit in Suit:
			for num in Number:
				self.cardList.append(Card(suit, num))
	
	def shuffle(self):
		shuffle(self.cardList)
	
	def draw(self):
		return self.cardList.pop(0)
	
	def __str__(self):
		s = ""
		for card in self.cardList:
			s += "%s," % card
		return s

# A hand is just a tiny deck that you don't shuffle, right?
class Hand(Deck):
	'Defines properties of a hand of playing cards'
	
	def __init__(self):
		self.cardList = []
	
	def addCard(self, card):
		self.cardList.append(card)
	
	# The value of a hand is the total value of all it's cards (using the optimal value of Aces)
	def getValue(self):
		i = 0
		aces = 0
		for card in self.cardList:
			if (card.getNumber() == Number.ACE):
				aces += 1
			i += card.getValue()
		# For Blackjack, make sure Aces count as the best possible value
		while (aces > 0 and i > 21):
			i -= 10
			aces -= 1
		return i
