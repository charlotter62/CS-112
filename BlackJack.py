import random

def instructions():
    print('''To play Black Jack, you will be dealt a 2 card hand. Cards number 10 or below are their face value, while Kings, Queens, and Jacks are worth 10. The goal of the game is to get a black jack value as close to 21 as you can without going over. After seeing the cards in your hand you will have the choice to hit (draw another card and boost your black jack value) or stand (to prevent risking going over 21). Let's begin!''')

def makeADeckOf52():
    NUM_OF_CARDS_IN_DECK=52
    deck= []
    decknum =[]
    while len(deck) < 52:
        num = random.randrange(1,NUM_OF_CARDS_IN_DECK +1)
        if num not in decknum:
            decknum.append(num)
            deck.append(Card(num))
    return(deck)
 

class Player:
    def __init__(self, n, g, h, b):
        self.name = n
        self.gameswon= g
        self.hand= h
        self.bjval = b
    def __str__(self):
        printHand = ""
        for card in self.hand:
            printHand+= str(card) + " "
        return(self.name + "'s hand: " + str(printHand) + ". (Black jack value: " + str(self.bjval) + ")")
    def getPlay(self):
        play = input("Would you like to hit or stand? (h/s) ")
        return(play)
        
class Card:
    def __init__(self, n):
        self.num = n
        self.suit = self.getCardsuit(n)
        self.rank = self.getCardrank(n)
        self.bjval = self.getBjValue(n)
    def getBjValue(self, n):
        if (n%13)+1 < 10:
            b = (n%13) + 1
        else:
            b = 10
        self.bjval = b
        return(b)
    def getCardsuit(self,num):
        if num//13 == 0:
            suit = "♣" 
        elif num//13 == 1:
            suit = "♦"
        elif num//13 ==2:
            suit = "♥"
        else:
            suit = "♠"
        return(suit)
    def getCardrank(self,num):
        rank = (num%13)+1
        if rank == 11:
            rank = "J"
        elif rank == 12:
            rank = "Q"
        elif rank == 13:
            rank = "K"
        return(rank)
    
    def __str__(self):
        return(str(self.rank) + str(self.suit))

def main():
    instructions()
    print(" ")

    name1 = input("Player 1 enter your name: ") 
    gameswon = 0
    hand = []
    bjval = 0
    player1 = Player(name1,gameswon,hand,bjval)

    name2 = input("Player 2 enter your name: ")
    gameswon = 0
    hand = []
    bjval = 0
    player2 = Player(name2,gameswon,hand,bjval)

    print(" ")

    deck = makeADeckOf52()
    keepGoing = "y"

    while keepGoing == "y":
        player1.bjval = 0 #re-initialize bjvalues for each player
        player2.bjval = 0

        deck = makeADeckOf52()
        (player1.bjval, player1.hand, deck) = turn(deck, player1.name)
        print(" ")
        
        deck = makeADeckOf52()
        (player2.bjval, player2.hand, deck) = turn(deck, player2.name)
        print(" ")

        print(player1)
        print(player2)
        print(" ")

        if player1.bjval == player2.bjval: # The players tie
            print(player1.name + " and " + player2.name + ", you tied this round!")   
        else:               
            if player1.bjval > 21 and player2.bjval >21: # They are both greater than 21
                if abs(player1.bjval-21) < abs(player2.bjval-21):
                    player = player1
                    player1.gameswon +=1
                elif abs(player2.bjval-21) < abs(player1.bjval-21):
                    player = player2
                    player2.gameswon +=1
                print((player).name + ", you both went over, but your black jack value was closest to 21. You win this round!")
            else:
                if player1.bjval <= 21 and player2.bjval <= 21: #They are both less than 21
                    if (21 - player1.bjval) < (21 - player2.bjval):
                        player = player1
                        player1.gameswon+=1
                    else:
                        player = player2
                        player2.gameswon+=1                   
                elif player1.bjval > 21 and player2.bjval <= 21: #player1 is greater than 21
                    player = player2
                    player2.gameswon+=1
                elif player2.bjval > 21 and player1.bjval <= 21: #player2 is greater than 21
                    player = player1
                    player1.gameswon+=1
                print((player).name + ", your black jack value was closest to 21 without going over. You win this round!")

        print(" ")
        print("Leaderboard: ")
        print(player1.name + ": " + str(player1.gameswon))
        print(player2.name + ": " + str(player2.gameswon))
        print('----------------------------------------------------------')
        keepGoing = input('Would you like to play another game? [y/n] ')
        print(" ")


def turn(deck,name):
    def dealAHand(deck):
        hand =[]                                 
        for count in range (0,2):
            hand.append(deck.pop())
        return(hand,deck)
    
    (hand,deck) = dealAHand(deck)

    def displayHand(hand):
        printHand = ""
        for card in hand:
            printHand+= str(card) + " "
        print(printHand)

    def bjHandValue(hand):
        n = []
        total = 0
        bj = 0
        for i in range(len(hand)):
            if ((hand[i].num)%13)+1 < 10:
                bj = ((hand[i].num)%13) + 1
            else:
                bj = 10
            total += bj 
        return(total)
    
    bjval = bjHandValue(hand)

    print(name + ", here is your hand:") 
    displayHand(hand)
    print("(Black jack value: " + str(bjval) + ")")
    print(" ")
    
    def getPlay():
        play = input("Would you like to hit or stand? (h/s) ")
        print(" ")
        return(play)

    play = "h"
    while bjval <=21 and play!= "s":
        play = getPlay()
        if play == "h":
            hand.append(deck.pop())
            bjval = bjHandValue(hand)
            print(("You drew " + str(hand[len(hand)-1])) + " (Updated black jack value: " + str(bjval) + ")")
            if bjval >21:
                print('Your black jack value is over 21, you went bust!')
    
    return(bjval, hand, deck)
    
    
      
