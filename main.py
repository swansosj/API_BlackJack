"""

This is an ongoing project to get more familiar with Python and APIs
with Python.

"""
#Import the request library to make the API call
import requests

#Prompt the user for how many decks they want
DeckAmount = input('How many decks of cards would you like in the pile? \nYour typical game of Blackjack has 8 decks\n')

#Creates empty dictionaries for the first request
payload = {}
headers = {'Accept': 'application/json'}
NewShuff = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(NewShuff, headers=headers, data=payload)

responseJSON = response.json()
DeckID = responseJSON['deck_id']

print("Your Deck id is: " + DeckID)

carddata = {}

DrawCard = "https://deckofcardsapi.com/api/deck/" + DeckID + "/draw/?count=1"

card = requests.get(DrawCard, headers=headers, data=carddata)

cardInfo = card.json()['cards'][0]

CardSuit = cardInfo['suit']
CardValue = cardInfo['value']


print(CardValue + " of " + CardSuit)
