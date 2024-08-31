#!python3
#Blackjack

import random
import sys
import time

#define characters
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
ALL_CHARACTERS = HEARTS,DIAMONDS,SPADES,CLUBS
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

def main():
    print("Welcome to 21")
    money = 100

    #main loop
    while money > 0:
        print("You have ", money, " dollars")
        playerInput = input("Place bet [Y/N]").upper()
        if playerInput == "N":
            print("You quit the game with ", money, " dollars to spare")
            sys.exit()
        #game loop
        money = gameLoop(money)
    print("You run out of money!")

def getDeck():
    deck = []
    for suit in ALL_CHARACTERS:
        for i in range(2,11):
            deck.append((str(i),suit))
        for i in ('J', 'Q', 'K', 'A'):
            deck.append((str(i),suit))
    random.shuffle(deck)
    return deck

def getHandValue(hand):
    value = 0
    aceCount = 0
    for i in hand:
        rank = i[0]
        # print("Rank value: ", rank)
        if rank == "A":
            aceCount += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)
    if aceCount > 0:
        value += aceCount
        for i in range(1,aceCount+1):
            if ((value + 10) <= 21):
                value += 10
    # print("Value of the following hand is: ", hand)
    # print("Amount of aces: ", aceCount)
    # print("Hand value is ", value)
    return value

def drawCards(cards):
    rows = ["", "", "", "", ""]
    for i,card in enumerate(cards):
        value = card[0]
        suit = card[1]
        # cards are 4*6
        rows[0] += ' ___  '.format()
        rows[1] += '|{} | '.format(value.ljust(2))
        rows[2] += '| {}| '.format(suit.ljust(2))
        rows[3] += '|__{} '.format(value.rjust(2), "_")

    for row in rows:
        print(row)

#single game loop
def gameLoop(money):
    bet = 20
    print("New game!")
    money = money - bet
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]
    print("Dealer: ")
    drawCards(dealerHand)
    print("Dealer value: ",getHandValue(dealerHand))
    print("Player: ")
    drawCards(playerHand)
    print("Player value: ",getHandValue(playerHand))
    if int(getHandValue(playerHand)) == 21:
        print("Blackjack! You win!")
        money += (bet * 2)
        return money 
    elif int(getHandValue(dealerHand)) == 21:
        print("Dealer has blackjack! You lose!")
        return money
    elif int(getHandValue(playerHand)) == 21 and int(getHandValue(dealerHand)) == 21:
        print("Its a draw!")
        money += bet
        return money

    playerInput = input("Hit [H] or Stand [S]:").upper()

    if playerInput == "H":
        newCard = deck.pop()
        print("You drew a new card")
        playerHand.append(newCard)
        drawCards(playerHand)
        if getHandValue(playerHand) > 21:
            print("You went bust! Value: ", getHandValue(playerHand))
            return money
    elif playerInput == "S":
        print("You stand")
    else:
        print("Input error!")
        sys.exit()

    if getHandValue(playerHand) < 21:
        while int(getHandValue(dealerHand)) < 17:
            newCard = deck.pop()
            print("Dealer draws ")
            dealerHand.append(newCard)
            drawCards(dealerHand)
            print("Dealer value: ", getHandValue(dealerHand))
            print("Player value: ", getHandValue(playerHand))

    if int(getHandValue(playerHand)) == 21 and int(getHandValue(dealerHand)) < 21:
        print("Blackjack! You win!")
        money += (bet * 2)
        return money
    if int(getHandValue(dealerHand)) > 21 or int(getHandValue(dealerHand)) < int(getHandValue(playerHand)):
        print("You win!")
        money += (bet * 2)
        return money
    elif getHandValue(dealerHand) == getHandValue(playerHand):
        print("Its a draw!")
        money += bet
        return money
    else:
        print("The dealer won!")
        return money

# start main loop
main()

