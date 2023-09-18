import random
deck_of_cards = {
    'hearts': ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH'],
    'diamonds': ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD'],
    'clubs': ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'],
    'spades': ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
}

def draw_card(deck_of_cards):
  suit = random.choice(list(deck_of_cards.keys()))  #key of deck of card which is suit and list is the numbers in random choice
  card = random.choice(deck_of_cards[suit]) # random card from the list within the suit 
  return card

def deal_cards():
  player_cards = []
  dealer_cards = []
  for i in range(2):  #  giving 2 cards 
    new_player_card = draw_card(deck_of_cards)
    new_dealer_card = draw_card(deck_of_cards)
    player_cards.append(new_player_card)
    dealer_cards.append(new_dealer_card)
    
  return player_cards, dealer_cards #dealer and player are pulling from the list of cards 
  

new_hand = deal_cards()  #deal_cards gives 2 cards 
print(new_hand)

def sum_of_cards():
    pass


print(f'You have {new_hand[0][0]} and {new_hand[0][1]}. Dealer has a {new_hand[0][1]} showing ')
user_choice = input('Do you want to hit or stay')
if user_choice == 'hit':
  player_cards= new_hand
  print('you hit ')

print(deck_of_cards)

