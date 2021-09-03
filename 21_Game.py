import random
import time
import os
def Clear_Screen():
    os.system("cls||clear")

Clear_Screen()

cards = []
users_cards = []
dealer_cards = []
user_bust = False
dealer_bust = False
debug = True


def reset_cards():
    global cards
    cards = []
    for suits in ["Heart","Diamond","Club", "Spade"]:
        for card in range(13):

            cards.append({"suits":suits,"card":card+1});
      
    
def get_card_name(number):
    if number == 13:
        return "Ace"
    elif number == 12:
        return "king"
    elif number == 11:
        return "Quean"
    elif number == 10:
        return "Jack"
    else:
        return number

def get_card_value(number,bust):
    if number > 9:
        if number == 13:
            if bust:
                return 1
            else:
                return 11
        else:
            return 10
    else:
        return number

def hit_or_stike_game():
    global user_bust
    global dealer_bust
    user_bust = False
    dealer_bust = False
    
    print("")
    print("Welcome to a game of 21. Good Luck")
    print("")
    reset_cards()
    print("The Dealer shuffle the card and start drawing the cards.")
    if(debug == False):
        time.sleep(5)
    draw_users_cards()
    draw_dealer_cards()
    user_turn()

def user_input_stick_twist(text):
    stick = ["s","stick"]
    twist = ["t","twist"]
    u_input = input(text).lower()
    if u_input in stick:
        return "s"
    elif u_input in twist:
        return "t"
    else:
        print("Invalid Input")
        return user_input_stick_twist(text);

def user_turn():
    global users_cards
    global user_bust
    print("")
    print("Your card are")
    print("")
    for item in range(len(users_cards)):
        print(f"{get_card_name(users_cards[item]['card'])} of {users_cards[item]['suits']}")
    print("")
    u_input = user_input_stick_twist("Stick or Twist: ")
    if u_input == "t":
        extra_card = draw_extra_users_card()
        print("The Dealer Drawing a card.")
        if(debug == False):
            time.sleep(5)

        if(get_total(users_cards,False) > 21 and get_total(users_cards,True) < 21):
            user_bust = True

        if get_total(users_cards,user_bust) > 21:
            print(f"Your extra card was {get_card_name(extra_card['card'])} of {extra_card['suits']}")
            print("You Lose!")
            if(debug == False):
                time.sleep(5)
            hit_or_stike_game()
        else:
            if len(users_cards) == 5:
                print("5 Card Trick!")
                print("You Win!")
                exit()
            else:
                user_turn()
    else:
        dealer_turn()
    

def dealer_turn():
    global dealer_cards
    global users_cards
    global user_bust
    global dealer_bust
    dealer_total = get_total(dealer_cards,dealer_bust)
    users_total = get_total(users_cards,user_bust)

    print("The Dealer flip his cards.")
    if(debug == False):
        time.sleep(3)
    
    print("")
    print("dealers card are")
    print("")
    for item in range(len(dealer_cards)):
        if(debug == False):
            time.sleep(1)
        print(f"{get_card_name(dealer_cards[item]['card'])} of {dealer_cards[item]['suits']}")
    
    print("Dealer is thinking")
    if(debug == False):
        time.sleep(5)
    if(get_total(dealer_cards,False) > 21 and get_total(dealer_cards,True) < 21):
            dealer_bust = True

    if dealer_total < 15 or get_total(dealer_cards,True) < 10:
        card = draw_extra_dealer_card()
        print(card)
        print("Dealer draws an extra card")
        if(debug == False):
            time.sleep(5)
        print(f"the Dealer extra card was {get_card_name(card['card'])} of {card['suits']}")

        dealer_turn()
    elif get_total(dealer_cards,dealer_bust) > 21:
        print("Dealer is bust")
        if(debug == False):
            time.sleep(5)

        print("You Win!")
        exit()
    else:
        if get_total(users_cards, user_bust) > 21:
            print("You Lose!")
            if(debug == False):
                time.sleep(5)
        elif get_total(dealer_cards, dealer_bust) > 21:
            print("You Win!")
            exit()
        elif users_total > dealer_total:
            print("You Win!")
            exit()
        elif users_total < dealer_total:
            print("You Lose!")
            if(debug == False):
                time.sleep(5)
            hit_or_stike_game()
        else:
            print("Draw. Sorry i mean you Lose!")
            if(debug == False):
                time.sleep(5)
            hit_or_stike_game()
    
def get_total(cards,bust):
    total = 0
    for item in cards:
        if item["card"] == 13:
            if bust:
                total = 1
            else:
                total = 11
        else:
            total += item["card"]
    return total
    

def draw_extra_users_card():
    global users_cards
    global cards
    card1_index = random.randint(0,len(cards)-1)
    card1= cards[card1_index]
    cards.pop(card1_index)
    users_cards.append(card1)
    return card1

def draw_extra_dealer_card():
    global dealer_cards
    global cards
    card1_index = random.randint(0,len(cards)-1)
    card1= cards[card1_index]
    cards.pop(card1_index)
    dealer_cards.append(card1)
    return card1


def draw_users_cards():
    global cards
    global users_cards

    card1_index = random.randint(0,len(cards)-1)

    card2_index = random.randint(0,len(cards)-1)
    while card1_index == card2_index:
        card2 = random.randint(0,len(cards)-1)


    card1 = cards[card1_index];
    card2= cards[card2_index]
    if card1_index < card2_index:
        cards.pop(card2_index)
        cards.pop(card1_index)
    else:
        cards.pop(card1_index)
        cards.pop(card2_index)

    users_cards = [card1,card2]

def draw_dealer_cards():
    global cards
    global dealer_cards

    card1_index = random.randint(0,len(cards)-1)

    card2_index = random.randint(0,len(cards)-1)
    while card1_index == card2_index:
        card2 = random.randint(0,len(cards)-1)


    card1 = cards[card1_index];
    card2 = cards[card2_index]
    
    if card1_index < card2_index:
        cards.pop(card2_index)
        cards.pop(card1_index)
    else:
        cards.pop(card1_index)
        cards.pop(card2_index)

    dealer_cards = [card1,card2]

hit_or_stike_game()