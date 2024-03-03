import art
import random

logo = art.logo
cards_dict = {"Ace": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Joker": 10, "Queen": 10, "King": 10}
cards_list = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Joker", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Joker", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Joker", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Joker", "Queen", "King"]

pl_cards_list = []
comp_cards_list = []
index = 51
pl_current_score = 0
comp_current_score = 0

def pick_card():
    global index
    global pl_current_score
    global comp_current_score

    pl_first_card_index = random.randint(0, index)
    index -= 1
    comp_first_card_index = random.randint(0, index)
    index -= 1
    pl_cards_list.append(cards_list[pl_first_card_index])
    pl_first_card_score = cards_dict[cards_list[pl_first_card_index]]
    pl_current_score += pl_first_card_score

    comp_cards_list.append(cards_list[comp_first_card_index])
    comp_first_card_score = cards_dict[cards_list[comp_first_card_index]]
    comp_current_score += comp_first_card_score


if input("Do you want to play a game Blackjack? Type 'yes' or 'no'.\n" ) == "yes":
    print(logo)
    pick_card()
    pick_card()

    while (pl_current_score <= 21 and comp_current_score <= 21):
        print(f"Your cards are {pl_cards_list}.\n Your current score is {pl_current_score}. \n Computer's first card is {comp_cards_list[0]}")

        inp =  input("Type 'yes' to get another card. Type 'no' to pass.\n")
        if (inp  == "yes"): 
            pick_card()
            print(f"Your final cards are {pl_cards_list}.\n Your final score is {pl_current_score}.\n Computers hand was {comp_cards_list}.\n Computers final score is {comp_current_score}. ")
        if (inp  == "no"): 
            print(f"Your cards are {pl_cards_list}.\n Your current score is {pl_current_score}. \n Computer's is {comp_cards_list}")
            if (pl_current_score > comp_current_score):
                print("Congrats, you won!")
            elif (pl_current_score == comp_current_score):
                print("No one wins..")
            else: 
                print("Sorry for your loss :( ")
            break
    
    else:
        if (comp_current_score > 21):
            print("Congrats, you won!")
        if (pl_current_score > 21):
            print("Sorry for your loss :( ")

