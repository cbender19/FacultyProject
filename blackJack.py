import sys
import random
import os
import time

deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
global total
global newTotal
add = 0
add2 = 0
temp = 0
temp2 = 0

n = 2
playerHand = random.sample(deck, n)
n = 1
dealerHand = random.sample(deck, n)

def rules():
    cmd = "clear"
    os.system(cmd)
    print("\n\t==========  Rules of the Game  ==========")
    print("")
    print("\t1.  Achieve \'21\' without going over.")
    print("\t2.  Beat the dealer to closest to \'21\'"
    "\n\twhithout going over.")
    print("\t3.  If you get \'21\' or closest to it,"
    "\n\tyou win.")
    print("\t4.  If the dealer gets \'21\' or closest"
    "\n\tto it, you lose.")
    print("\t5.  All \'J\', \'Q\', \'K\' equal 10.")
    print("\t6.  All \'A\' are either 11 or 1.")
    print("")
    print("\t\t\tGood Luck!")
    print("\t=========================================")

def start():
    question = "\n\tAre you ready to play? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(y/n): ')).lower().strip()
        if reply[0] == 'y':
            drawCards()
            break
        elif reply[0] == 'n':
            print("\n\t\t\tHave a good day!\n")
            print("\t=========================================")
            time.sleep(3)
            cmd = 'clear'
            os.system(cmd)
            exit(1)
        else:
            print("\t\t\tSorry, didn't catch that.")

def drawCards():
    print("")
    print("\t=========================================")
    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")

    if(playerHand[0] == 'A' and playerHand[1] == 'J' or playerHand[0] == 'A' and playerHand[1] == 'Q' or playerHand[0] == 'A' and playerHand[1] == 'K'):
        #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
    elif(playerHand[0] == 'J' and playerHand[1] == 'A' or playerHand[0] == 'Q' and playerHand[1] == 'A' or playerHand[0] == 'K' and playerHand[1] == 'A'):
        #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
    else:
        decision()

def decision():
    print("\t=========================================")
    question = "\n\tDo you want to hit or stay? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(h/s): ')).lower().strip()
        if reply[0] == 'h':
            print("")
            print("\t=========================================")
            hit(add)
            break
        elif reply[0] == 's':
            print("\n\t\t      Dealers turn.")
            dealer()
            break
        else:
            print("\t\tSorry, didn't catch that.")

def hit(add):
    n = 1

    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")

    global count
    if playerHand[0] == 'A':
        ace(total, newTotal)
    elif playerHand[0] == '2':
        count = 2
        #playerHand.append(2)
    elif playerHand[0] == '3':
        count = 3
        #playerHand.append(3)
    elif playerHand[0] == '4':
        count = 4
        #playerHand.append(4)
    elif playerHand[0] == '5':
        count = 5
        #playerHand.append(5)
    elif playerHand[0] == '6':
        count = 6
        #playerHand.append(6)
    elif playerHand[0] == '7':
        count = 7
        #playerHand.append(7)
    elif playerHand[0] == '8':
        count = 8
        #playerHand.append(8)
    elif playerHand[0] == '9':
        count = 9
        #playerHand.append(9)
    elif playerHand[0] == '10':
        count = 10
        #playerHand.append(10)
    elif playerHand[0] == 'J':
        count = 10
        #playerHand.append(10)
    elif playerHand[0] == 'Q':
        count = 10
        #playerHand.append(10)
    elif playerHand[0] == 'K':
        count = 10
        #playerHand.append(10)

    global count2
    if playerHand[1] == 'A':
        ace(total, newTotal)
    elif playerHand[1] == '2':
        count2 = 2
    elif playerHand[1] == '3':
        count2 = 3
    elif playerHand[1] == '4':
        count2 = 4
    elif playerHand[1] == '5':
        count2 = 5
    elif playerHand[1] == '6':
        count2 = 6
    elif playerHand[1] == '7':
        count2 = 7
    elif playerHand[1] == '8':
        count2 = 8
    elif playerHand[1] == '9':
        count2 = 9
    elif playerHand[1] == '10':
        count2 = 10
    elif playerHand[1] == 'J':
        count2 = 10
    elif playerHand[1] == 'Q':
        count2 = 10
    elif playerHand[1] == 'K':
        count2 = 10

    total = count + count2
    temp2 == total

    global count3
    global temp3
    hit = random.sample(deck,n)
    if hit[0] == 'A':
        ace(total, newTotal)
    elif hit[0] == '2':
        count3 = 2
        newTotal = total + count3
    elif hit[0] == '3':
        count3 = 3
        newTotal = total + count3
    elif hit[0] == '4':
        count3 = 4
        newTotal = total + count3
    elif hit[0] == '5':
        count3 = 5
        newTotal = total + count3
    elif hit[0] == '6':
        count3 = 6
        newTotal = total + count3
    elif hit[0] == '7':
        count3 = 7
        newTotal = total + count3
    elif hit[0] == '8':
        count3 = 8
        newTotal = total + count3
    elif hit[0] == '9':
        count3 = 9
        newTotal = total + count3
    elif hit[0] == '10':
        count3 = 10
        newTotal = total + count3
    elif hit[0] == 'J':
        count3 = 10
        newTotal = total + count3
    elif hit[0] == 'Q':
        count3 = 10
        newTotal = total + count3
    elif hit[0] == 'K':
        count3 = 10
        newTotal = total + count3

    if newTotal == 21:
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
        #playAgain()

    elif newTotal > 21:
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t       Busted!")
        print("\t\t====  You Lose!  ====")
        #playAgain()

    else:
        add += newTotal
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(add))
        temp == add
        nextHit()

def nextHit():
    print("\t=========================================")
    question = "\n\tDo you want to hit or stay? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(h/s): ')).lower().strip()
        if reply[0] == 'h':
            print("")
            print("\t=========================================")
            hit(add)
            break
        elif reply[0] == 's':
            print("\n\t\t      Dealers turn.")
            dealer(hit, add)
            break
        else:
            print("\t\tSorry, didn't catch that.")

def dealer(hit, add):
    print("\t=========================================")
    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")
    #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(add))

    n = 1
    dealerHand2 = random.sample(deck, n)
    hand = str(dealerHand)[1:-1] +", " +str(dealerHand2)[1:-1]

    count = 0
    if dealerHand[0] == 'A':
        count = 11
    elif dealerHand[0] == '2':
        count = 2
    elif dealerHand[0] == '3':
        count = 3
    elif dealerHand[0] == '4':
        count = 4
    elif dealerHand[0] == '5':
        count = 5
    elif dealerHand[0] == '6':
        count = 6
    elif dealerHand[0] == '7':
        count = 7
    elif dealerHand[0] == '8':
        count = 8
    elif dealerHand[0] == '9':
        count = 9
    elif dealerHand[0] == '10':
        count = 10
    elif dealerHand[0] == 'J':
        count = 10
    elif dealerHand[0] == 'Q':
        count = 10
    elif dealerHand[0] == 'K':
        count = 10

    count2 = 0
    if dealerHand2[0] == 'A':
        count2 == 11
    elif dealerHand2[0] == '2':
        count2 = 2
    elif dealerHand2[0] == '3':
        count2 = 3
    elif dealerHand2[0] == '4':
        count2 = 4
    elif dealerHand2[0] == '5':
        count2 = 5
    elif dealerHand2[0] == '6':
        count2 = 6
    elif dealerHand2[0] == '7':
        count2 = 7
    elif dealerHand2[0] == '8':
        count2 = 8
    elif dealerHand2[0] == '9':
        count2 = 9
    elif dealerHand2[0] == '10':
        count2 = 10
    elif dealerHand2[0] == 'J':
        count2 = 10
    elif dealerHand2[0] == 'Q':
        count2 = 10
    elif dealerHand2[0] == 'K':
        count2 = 10

    total = count + count2
    if total == 21:
        print("\t\t\t\t" +hand +"  is: " +str(total))
        print("\n\t\t====  Dealer Wins!!  ====")
        #playAgain()
    else:
        hit = random.sample(deck,n)

        newTotal = 0
        count3 = 0
        if hit[0] == 'A':
            count3 == 11
            newTotal = total + count3
        elif hit[0] == '2':
            count3 = 2
            newTotal = total + count3
        elif hit[0] == '3':
            count3 = 3
            newTotal = total + count3
        elif hit[0] == '4':
            count3 = 4
            newTotal = total + count3
        elif hit[0] == '5':
            count3 = 5
            newTotal = total + count3
        elif hit[0] == '6':
            count3 = 6
            newTotal = total + count3
        elif hit[0] == '7':
            count3 = 7
            newTotal = total + count3
        elif hit[0] == '8':
            count3 = 8
            newTotal = total + count3
        elif hit[0] == '9':
            count3 = 9
            newTotal = total + count3
        elif hit[0] == '10':
            count3 = 10
            newTotal = total + count3
        elif hit[0] == 'J':
            count3 = 10
            newTotal = total + count3
        elif hit[0] == 'Q':
            count3 = 10
            newTotal = total + count3
        elif hit[0] == 'K':
            count3 = 10
            newTotal = total + count3

        print("\t\t\t\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))

        if newTotal == 21:
            #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
            print("\n\t\t====  You Lose!  ====")
            #playAgain()

        elif newTotal > 21:
            #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
            print("\n\t\t    Dealer Busted!")
            print("\t\t====  You Win!!  ====")
            #playAgain()
        else:
            determineWinner(newTotal, temp, temp2)

def ace(total, newTotal):
    question = "\n\tYou have an Ace, do you want to make that a 1 or an 11? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(1/11): ')).lower().strip()
        if reply[0] == '1':
            count, count2, count3 = 1
            newTotal = total + 1
            break
        elif reply[0] == '11':
            count, count2, count3 = 11
            newTotal = total + 11
            break
        else:
            print("\t\t\tSorry, didn't catch that.")

def determineWinner(newTotal, temp, temp2):
    if temp > newTotal:
        print("\n\t\t====  You Win!!  ====")
    elif temp2 > newTotal:
        print("\n\t\t====  You Win!!  ====")
    else:
        print("\n\t\t====  You Lose!  ====")

def playAgain():
    question = "\n\tWant to play again? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(y/n): ')).lower().strip()
        if reply[0] == 'y':
            cmd = 'python3 blackJack.py'
            os.system(cmd)
            break
        elif reply[0] == 'n':
            print("\n\t\t\tHave a good day!\n")
            print("\t=========================================")
            time.sleep(3)
            cmd = 'clear'
            os.system(cmd)
            exit(1)
        else:
            print("\t\t\tSorry, didn't catch that.")

def main(argv):
    rules()
    start()
    playAgain()

if __name__ == "__main__":
    main(sys.argv)
