#  card.py
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



from enum import Enum

class Suit(Enum):
	CLUBS = 4
	DIAMONDS = 3
	HEARTS = 2
	SPADES = 1

# Because Python ignores enum names that have the same value as another name, I've done this crime
# It's "fixed" in the getValue() method of Card
class Number(Enum):
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14

class Card:
	'Defines the properties a standard playing card object'
	
	def __init__(self, s, n):
		self.suit = s
		self.number = n
	
	def getValue(self):
		if (self.number.name == "ACE"): # Fixes the value of Ace cards
			return 11
		elif (self.number.name in ["JACK", "QUEEN", "KING"]): # Fixes the value of other face cards
			return 10
		return self.number.value
	
	def getSuit(self):
		return self.suit
	
	def getNumber(self):
		return self.number
	
	# Returns "NUMBER of SUIT"
	def __str__(self):
		return '%s of %s' % (self.number.name, self.suit.name)
	
	# Since __cmp__ is depreciated in Python3, I'll use this instead
	def __eq__(self, x): 
		return self.suit == x.suit and self.number == x.number
