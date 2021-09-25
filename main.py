import art
import random
import os

def show_art():
    """Draw the asci art - takes no arguments"""
    print(art.logo)

def draw_card():
    """Returns a random card from a predifined 
    list of cards, and takes no arguments"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_hand(hand):
    """Calculates the final score of a list of cards
     - Takes a single list of arguments"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:  
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def computer_plays(hand):
    """Function to play as the computer - Takes 1 argument Computer Hand"""
    while calculate_hand(hand) < 17:
        hand.append(draw_card())
    return hand

def compare_hands(player_score, computer_score):
    """This function checks the score and prints 
    out directly to the screen if you won the game"""
    if player_score == computer_score:
        print("It is a Draw!")
    elif player_score == 0:
        print("Black Jack, your Win!")
    elif computer_score == 0:
        print("You Lose!, Computer got Black Jack")
    elif player_score <= 21 and computer_score <= 21 and player_score > computer_score:
        print("You Win!")
    elif computer_score <= 21 and player_score <= 21 and computer_score > player_score:
        print("You Lose!")
    elif player_score > 21:
        print("You Lose!")
    elif computer_score > 21 and player_score <= 21:
        print("You Win!")

def main_loop():
        os.system('clear')
        show_art()
        player_hand = list()
        computer_hand = list()
        active = True
        for _ in range(2):
            player_hand.append(draw_card())
            computer_hand.append(draw_card())

        print(f"Your cards: {player_hand}, current score: {calculate_hand(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
        while active:
            if calculate_hand(player_hand) < 22:
                if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                    
                    player_hand.append(draw_card())
                    print(f"Your cards: {player_hand}, current score: {calculate_hand(player_hand)}")
                    print(f"Computer's first card: {computer_hand[0]}")
                else:
                    active = False
                    new_cop_hand = computer_plays(computer_hand)
                    print(f"Your cards: {player_hand}, current score: {calculate_hand(player_hand)}")
                    print(f"Computer cards: {new_cop_hand}, current score: {calculate_hand(new_cop_hand)}")
                    compare_hands(calculate_hand(player_hand), calculate_hand(new_cop_hand))
            else:
                print("You are over 21 and you Lose!")
                active = False
        else:
            if input("Do you want to play another game of Blackjack? Type 'y' or 'n'").lower() == 'y':
                main_loop()
            else:
                print("Good Bye")


if __name__ == "__main__":
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if answer == 'y':
        main_loop()
    else:
        print('Good Bye')