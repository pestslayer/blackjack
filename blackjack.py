from random import randint
"""
two players
52 cards 4 suits clubs, hearts, diamonds, spades, 
cards numbered 1 - 13 
random shuffle 
see own cards but not dealers 
count cards if num > 21 bust 
21 on first draw 'blackjack'
hit, bust, stand
once stand you can see dealers cards 
dealer can bust 
closest to 21 wins 
"""
class Blackjack:
    
    def __init__(self,player, dealer, cards):
        self.player = player
        self.dealer = dealer
        self.cards = cards 

    
    def player1(self):
        self.player = 0
        card1 = randint(1,10)
        card2 = randint(1,10)
        card_sum = card1 + card2 
        print(f'Your cards are {card1} and {card2} = {card_sum}')
        if card1 + card2 == 21:
            print('BlackJack!')
        cards = [card1,card2]
        while self.player  < 22:
            msg = input("Would you like to stand or hit? ")
            if msg.lower() == 'hit':
                card3 = randint(1,10)
                cards.append(card3)
                card_sum = sum(cards)
                self.player = card_sum
                print(f"Your cards are {cards} = {card_sum}")
            elif msg.lower() == 'stand':
                self.player = card_sum
                return None
        if self.player > 21:
            print("Bust")
            return total 
    def deal(self):
        self.dealer = 0
        deal_card = randint(1,10)
        deal_card1 = randint(1,10)
        dealer_total = deal_card + deal_card1
        while dealer_total < 15:
            deal_card2 = randint(1,10)
            new_dealer_total = deal_card + deal_card1 + deal_card2
            dealer_total = new_dealer_total
        self.dealer = dealer_total
        if self.dealer > 21:
            print("Dealer Bust!")
            return None


    def who_wins(self):
        print(f'The dealer had {self.dealer}')
        if self.dealer > 21:
            print("Dealer Bust")
            return None
        if self.player == self.dealer:
            print("You lose!")
            return None
        elif self.player > 21:
            print("You lose!")
            return None
        elif self.player > self.dealer:
            print("You win!")
            return self.player
        else: 
            print("Dealer wins")
            return self.player
        
        
        
play = Blackjack(0,0,0)

def run():
    while True:
        again = input("Would you like to play ")
        if again.lower() == "yes":
            play.player1()
            play.deal()
            play.who_wins()  
        elif again.lower() == "no":
            return False
        else:
            print("Please type 'yes' or 'no' ")
        

run()
        

