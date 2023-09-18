import random

playerin=True
dealerin=True

deck=(2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
      'A','K','Q','J','A','K','Q','J','A','K','Q','J','A','K','Q','J')

playerHand=[]
dealerHand=[]

#deal cards

def dealcard(turn):
    card=random.choice(deck)
    turn.append(card)

#total of each hand
def total(turn):
    total = 0 
    face =['K','Q','J']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total +=1
            else:
                total += 11
    return total

# check for winner
def showdealer_hand():
    if len(dealerHand) ==2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0],[1]
    

#game loop
for i in range(2):
    dealcard(dealerHand)
    dealcard(playerHand)

print(dealerHand)
print(playerHand)


while playerin or dealerin:
    print(f'dealer has {showdealer_hand()} and ? ')
    print(f'you have{playerHand}={total(playerHand)}')
    if playerin:
        stayothit= input(' [s]tay or [H]it ').lower()
        if total(dealerHand) > 16:
            dealerin = False
        else:
            dealcard(dealerHand)
        if stayothit == 's':
            playerin= False
        else:
            dealcard(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

if total(playerHand) == 21:
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has {total(dealerHand)} ')
    print(" you have blackjack ")
elif total(dealerHand)==21:
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has {total(dealerHand)} ')
    print(" Dealer has blackjack ")
elif total(playerHand) > 21:
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has {total(dealerHand)} ')
    print(" you bust dealer win ")
elif total(dealerHand)>21:
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has {total(dealerHand)} ')
    print(" dealer bust you win ")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has{total(dealerHand)}')
    print(" Dealer Wins")
elif 21- total(dealerHand) > 21 -total(playerHand):
    print(f'you have {playerHand} for a total of {total(playerHand)} and the dealer has{total(dealerHand)}')
    print(" You win")
        


