import os
import random

from art import logo

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def new_game():
    # we print the ascii art 
    print(f"\n\n{logo}")

    # next thing that we do is that we generate 2 cards for the player and then sum them up to show the user
    player_1_cards = [random.randint(1,10),random.randint(1,10)]
    player_1_cards_sum = sum(player_1_cards)

    # we show the player's cards and next we select the cards for the computer but then we show just the computer's first card
    print(f"Your cards: {player_1_cards}")

    computer_cards = [random.randint(1,10),random.randint(1,10)]
    computer_cards_sum = sum(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")

    get_another_card = input("Type 'y' to get another card,type 'n' to pass: ")

    if get_another_card == 'y':
        # we give the player another card
        player_1_cards.append(random.randint(1,10))
        # we update the sum
        player_1_cards_sum = sum(player_1_cards)

        # we check if after adding the card to the player's cards,the sum of the player's cards is still less then 21, if it's less 
        # than 21, we compare it to the computer's cards and figure something out 
        # if it's greater than 21 and the computer's cards is less than 21, the player loses

        if player_1_cards_sum > 21 and (computer_cards_sum) <=21 : 
            print(f"Your final hand: {player_1_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print("Computer Wins!!!")

        elif player_1_cards_sum < 21:
            # we then ask him if he wants to take another card again       
            get_another_card= input("Type 'y' to get another card,type 'n' to pass: ")
            if get_another_card == 'y':
                # we give the player another random card 
                player_1_cards.append(random.randint(1,10))
                # we update the sum 
                player_1_cards_sum = sum(player_1_cards_sum)
                if player_1_cards_sum > 21 and (computer_cards_sum) <=21 : 
                    print(f"Your final hand: {player_1_cards}")
                    print(f"Computer's final hand: {computer_cards}")
                    print("Computer Wins!!!")

    elif get_another_card == 'n':
        # we show our final hand 
        print(f"Your final hand: {player_1_cards}")
        print(f"Computer's final hand: {computer_cards}")

        if player_1_cards_sum > 21 and (computer_cards_sum <= 21):
            print("Computer Wins!!!")

        # if they are both under 21, we make the person whose number is closest to 21 win
        elif player_1_cards_sum <= 21 and (computer_cards_sum <= 21):
            if player_1_cards_sum > computer_cards_sum:
                print("You Win!!!")
            elif player_1_cards_sum < computer_cards_sum:
                print("Computer Wins!!!")
            else:
                print("Draw")


    
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
# if we type 'y', clear the console and load the ascii art and continue executing the rest of the code
if play_game == 'y':
    clear_console()
    new_game()

