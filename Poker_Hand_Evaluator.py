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
   def Find_Suits(dc):
    CardSpecies = [0] * 4  # ♣, ♥, ♦, ♠

    for check_card in dc:
        if '\u2663' in check_card:  # ♣
            CardSpecies[0] += 1
        elif '\u2665' in check_card:  # ♥
            CardSpecies[1] += 1
        elif '\u2666' in check_card:  # ♦
            CardSpecies[2] += 1
        elif '\u2660' in check_card:  # ♠
            CardSpecies[3] += 1

    return 5 in CardSpecies

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
    # 🎴 Deck of Cards
    Cards = ["A♣", "A♥", "A♦", "A♠",
             "2♣", "2♥", "2♦", "2♠",
             "3♣", "3♥", "3♦", "3♠",
             "4♣", "4♥", "4♦", "4♠",
             "5♣", "5♥", "5♦", "5♠",
             "6♣", "6♥", "6♦", "6♠",
             "7♣", "7♥", "7♦", "7♠",
             "8♣", "8♥", "8♦", "8♠",
             "9♣", "9♥", "9♦", "9♠",
             "10♣", "10♥", "10♦", "10♠",
             "J♣", "J♥", "J♦", "J♠",
             "Q♣", "Q♥", "Q♦", "Q♠",
             "K♣", "K♥", "K♦", "K♠"]

    # 🏆 Card Rankings
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

    # 🧠 Συνάρτηση αξιολόγησης χεριού
    def evaluate_hand(name, hand):
        print(f"\n{name} HAND: {hand}")
        if Find_Suits(hand):
            rank = CheckFlush(hand)
        else:
            rank = Check_Other_Rankings(hand)
        print(f"{name} RANK: {WinRankDict[rank]}")
        return rank

    # 🎮 Παίκτης
    player_hand = ['10♠', '10♣', '10♥', 'K♦', 'K♠']
    player_rank = evaluate_hand("PLAYER", player_hand)

    # 🧑‍⚖️ Dealer
    dealer_hand = ['Q♠', '10♠', 'J♠', 'K♠', 'A♠']
    dealer_rank = evaluate_hand("DEALER", dealer_hand)

    # 🥇 Ανακοίνωση νικητή
    if dealer_rank < player_rank:
        print(f"\n🏆 DEALER wins with {WinRankDict[dealer_rank]}")
    elif dealer_rank > player_rank:
        print(f"\n🏆 PLAYER wins with {WinRankDict[player_rank]}")
    else:
        print(f"\n🤝 It's a tie with {WinRankDict[player_rank]}")

if __name__ == '__main__':
    main()





