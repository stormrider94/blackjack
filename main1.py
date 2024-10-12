import os
import random

from art import logo

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# function to start a new game 
def new_game():
    # let's initialize the list that is going to contain the cards
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    #we print the logo 
    print(f"\n\n{logo}")
    player_cards = random.choices(cards,k=2)
    computer_cards = random.choices(cards,k=2)

    player_cards_sum = sum(player_cards)
    computer_cards_sum = sum(computer_cards)
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    player_keep_drawing_card = True
    while player_keep_drawing_card:
        get_another_card = input("Type 'y' to get another card,type 'n' to pass: ")
    

        # I need to call a function that keeps on asking to get another card until the person hits 'n'
        if get_another_card == 'y':
            new_card = random.choice(cards)
            player_cards.append(new_card)
            player_cards_sum = sum(player_cards)
            computer_cards_sum = sum(computer_cards)

            if ((player_cards_sum > 21) and (computer_cards_sum <=21)):
                print(f"Your final hand: {player_cards}")
                print(f"Computer's final hand: {computer_cards}")
                print("Computer Wins!!!")

                # we start the game all over
                start_game()
            # before we ask the user if he or she wants to get another card, we need to show the player his cards
            print(f"Your cards: {player_cards}")

        elif get_another_card == 'n':
            # set player_keep_drawing_card to False so that we can exit the player's turn and just  move to the computer's turn
            player_keep_drawing_card = False
        
    # After exiting the while loop, meaning the player's turn is over and it's now the computer's turn
    # computer's turn(dealer's turn)

    # if the sum of the computer's cards is less than 17, we have to force computer to draw another card 
    while computer_cards_sum < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_cards_sum=sum(computer_cards)

    # once the sum of the computer's cards becomes greater than 17, we have to compare the player's cards and the computer's card
    # to figure out who wins.
    if ((computer_cards_sum > 21) and (player_cards_sum <= 21)):
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand: {computer_cards}")
        print("You win!!!")
    elif (computer_cards_sum <= 21) and (player_cards_sum <=21):
        # if the computer's card's sum is greater than that of the player_cards_sum, computer wins 
        if computer_cards_sum > player_cards_sum:
            print(f"Your final hand: {player_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print("Computer Wins!!!")

            # then we start a new game
        elif player_cards_sum > computer_cards_sum:
            print(f"Your final hand: {player_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print("You Win!!!")
        
        else:
            # meaning both player and computer have the same value
            print(f"Your final hand: {player_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print("It's a draw!!!")
        
        
    # then we start a new game
    start_game()


                

        

def start_game():   
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    # if we type 'y', clear the console and load the ascii art and continue executing the rest of the code
    if play_game == 'y':
        clear_console()
        new_game()

    elif play_game == 'n':
        clear_console()
        quit()

start_game()
