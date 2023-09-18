import random

class BlackjackGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.deck = (
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            'A', 'K', 'Q', 'J',
            'A', 'K', 'Q', 'J',
            'A', 'K', 'Q', 'J',
            'A', 'K', 'Q', 'J',
        )
        self.player_in = True
        self.dealer_in = True

        # Deal initial cards
        for _ in range(2):
            self.deal_card(self.dealer_hand)
            self.deal_card(self.player_hand)

        print(f"Dealer's hand: {self.show_dealer_hand()} and ?")
        print(f"Your hand: {self.player_hand} = {self.total(self.player_hand)}")

        while self.player_in or self.dealer_in:
            if self.player_in:
                stay_or_hit = input('[S]tay or [H]it: ').lower()
                if stay_or_hit == 's':
                    self.player_in = False
                else:
                    self.deal_card(self.player_hand)

                if self.total(self.dealer_hand) > 16:
                    self.dealer_in = False
                else:
                    self.deal_card(self.dealer_hand)

                if self.total(self.player_hand) >= 21:
                    break
                elif self.total(self.dealer_hand) >= 21:
                    break

        player_total = self.total(self.player_hand)
        dealer_total = self.total(self.dealer_hand)

        print(f'Your hand: {self.player_hand} = {player_total}')
        print(f'Dealer hand: {self.dealer_hand} = {dealer_total}')

        if player_total == 21:
            print("You have blackjack!")
        elif dealer_total == 21:
            print("Dealer has blackjack!")
        elif player_total > 21:
            print("You bust, dealer wins!")
        elif dealer_total > 21:
            print("Dealer busts, you win!")
        elif 21 - dealer_total < 21 - player_total:
            print("Dealer wins!")
        elif 21 - dealer_total > 21 - player_total:
            print("You win!")

    def deal_card(self, turn):
        card = random.choice(self.deck)
        turn.append(card)

    def total(self, turn):
        total = 0
        face_cards = ['K', 'Q', 'J']

        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face_cards:
                total += 10
            elif card == 'A':
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    def show_dealer_hand(self):
        if len(self.dealer_hand) == 2:
            return self.dealer_hand[0]
        elif len(self.dealer_hand) > 2:
            return self.dealer_hand[0], self.dealer_hand[1]


game = BlackjackGame()