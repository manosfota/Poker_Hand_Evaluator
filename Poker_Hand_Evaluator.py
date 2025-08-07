from functools import reduce
import random as rd
from collections import Counter

def Dealer_Cards(Cards):
    d_card=[]
    for i in range(5):
        d_card.append(Cards.pop(rd.randrange(len(Cards))))   
    print("\nDEALER CARDS :",d_card,"\n")
    return d_card

def Players_Cards(Cards):
    print("\n--PLAYER CARDS--\n")
    p1_card=[]
    for i in range(2):
        p1_card.append(Cards.pop(rd.randrange(len(Cards))))
    print(p1_card)
    p2_card=[]
    for i in range(2):
        p2_card.append(Cards.pop(rd.randrange(len(Cards))))
    print(p2_card)
    return p1_card,p2_card

def Find_Suits(dc): 
    CardSpecies=[0]*4                          #  Create a list with 4 zero elements [0,0,0,0]
    for check_card in dc:
        if '\u2663' in check_card:             # If I have this specific kind ('\u2663') through the Dealer Cards  increase by 1 the variable CardSpecies[i]
            CardSpecies[0]=CardSpecies[0]+1
        elif '\u2665' in check_card:
            CardSpecies[1]=CardSpecies[1]+1
        elif '\u2666' in check_card:
            CardSpecies[2]=CardSpecies[2]+1
        elif '\u2660' in check_card:
            CardSpecies[3]=CardSpecies[3]+1
    
    if (5 in CardSpecies):                    # If there is the element 5 in the list it means that I have 5 same kinds
        print("I have got 5 same kind \n") 
        all_same_kind=True
    else: 
        print("I have't got 5 same kind\n") 
        all_same_kind=False


    # I just print the number of kind from the Dealer's Card 
    print("- \u2663 ==", CardSpecies[0])    
    print("- \u2665 ==", CardSpecies[1])
    print("- \u2666 ==", CardSpecies[2])
    print("- \u2660 ==", CardSpecies[3])
    print("\n")

    return all_same_kind

def SortedCards(dc):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']   # figure Deck Card

    sort_map = {c: i for i, c in enumerate(card_order)}    # enumerate the card_order list starting by zero (0:2, 1:3, 2:4)
    SortedCards = sorted(dc,key=lambda card: (sort_map[card[:-1]]))

    flag=True
    HighCard=None
    CheckCardPrev=sort_map[SortedCards[0][:-1]]
    for i in range(1,5):                
        CheckCardCur=(sort_map[SortedCards[i][:-1]])
        if ((CheckCardCur-CheckCardPrev)!=1):
            flag=False
            break
        else:
            CheckCardPrev= CheckCardCur            
    HighCard=SortedCards[4]
 
    return SortedCards,flag,HighCard

def CheckFlush(dc):    
    sorted_candidates, flag, HighCard = SortedCards(dc)
    
    if (flag):
        if (HighCard[:-1]=='A'):
            return 1
        else:
            return 2
    else:
        return 5
  
def Check_Other_Rankings(dc):
    sorted_candidates, flag, HighCard = SortedCards(dc)
    for current_card in range(len(dc)):
        dc[current_card]=dc[current_card][:-1]
    counter_dict=Counter(dc)

    card_counts= counter_dict.most_common(2)
    card1, card2=card_counts[0], card_counts[1] if len(card_counts) > 1 else (None, (None))

    if   (card1[1]==4):
        print ("Four of a kind")
        return 3
    elif ((card1[1]==3) and (card2[1]==2)):
        print ("Full House")
        return 4
    elif (card1[1]==3):
        print ("Three of a kind")
        return 7   
    elif ((card1[1]==2) and (card2[1]==2)):
        print ("Two Pair")
        return 8
    elif (card1[1]==2):
        print ("Pair")
        return 9
    elif (flag):
        print ("Straight")
        return 6
    else:
        print ("High Card: ",HighCard)
        return 10

def main():

# Deck of Cards 
    Cards=["A\u2663", "A\u2665", "A\u2666", "A\u2660",
           "2\u2663", "2\u2665", "2\u2666", "2\u2660",
           "3\u2663", "3\u2665", "3\u2666", "3\u2660",
           "4\u2663", "4\u2665", "4\u2666", "4\u2660",
           "5\u2663", "5\u2665", "5\u2666", "5\u2660",
           "6\u2663", "6\u2665", "6\u2666", "6\u2660", 
           "7\u2663", "7\u2665", "7\u2666", "7\u2660",
           "8\u2663", "8\u2665", "8\u2666", "8\u2660",
           "9\u2663", "9\u2665", "9\u2666", "9\u2660",
           "10\u2663","10\u2665","10\u2666","10\u2660",
           "J\u2663", "J\u2665", "J\u2666", "J\u2660",
           "Q\u2663", "Q\u2665", "Q\u2666", "Q\u2660",
           "K\u2663", "K\u2665", "K\u2666", "K\u2660"]
    
# Dictionary showing the hierarchy of cards 
    WinRankDict = {
    1:  "-- ROYAL FLUSH --",
    2:  "-- STRAIGHT FLUSH --",
    3:  "-- FOUR OF A KIND --",
    4:  "-- FULL HOUSE --",
    5:  "-- FLUSH --",
    6:  "-- STRAIGHT --",
    7:  "-- THREE OF A KIND --",
    8:  "-- TWO PAIR --",
    9:  "-- PAIR --",
    10: "-- HIGH CARD --"
}
    

#Player Cards Shuffling 
    pc=Dealer_Cards(Cards) 
    pc=['10♠', '10♣', '10♥', 'K♦', 'K♠']
    if (Find_Suits(pc)):
        WinRankPlayer=CheckFlush(pc)
    else:
        WinRankPlayer=Check_Other_Rankings(pc)
    print(WinRankDict[WinRankPlayer])



#Dealer Card Shuffling
    dc=Dealer_Cards(Cards) 
    dc=['Q♠', '10♠', 'J♠', 'K♠', 'A♠']
    if (Find_Suits(dc)):
        WinRankDealer=CheckFlush(dc)
    else:
        WinRankDealer=Check_Other_Rankings(dc)
    print(WinRankDict[WinRankDealer])


#Checking Card Ranking 
    if (WinRankDealer < WinRankPlayer):
        print("The Dealer wins with",WinRankDict[WinRankDealer] )
    else:
        print("The Player wins",WinRankDict[WinRankPlayer])


if __name__=='__main__':
    main()




