import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2: # Check for Blackjack
        return 0 # Blackjack is represented by 0 in this game  # user or computer gets a blackjack, they win immediately 

    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # If the score is over 21 and there's an Ace, convert it to 1
        cards.append(1) # using the  remove function of the list to remove the 11 and then appending 1 to the list

    return sum(cards)

# sum function is used to calculate the total score of the cards .  Can put a iterable like a list or tuple in the sum function and it will return the total sum of all the elements in that iterable.
# sum(interable, start=0) where start is the initial value to which the sum is added. If not specified, it defaults to 0.

# already have declared the varibales user_score and computer_score outside so cann't use them as parameters in the function, so used u_score and c_score as parameters
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0: # If the computer has a Blackjack user loses 
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0: # If the user has a Blackjack they win
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1 # Initialize scores to -1 to indicate they haven't been calculated yet
    # We can also use None to indicate that the score has not been calculated yet, declared them outside so that they can be accessed in the while loop
    user_score = -1
    is_game_over = False

    for _ in range(2):  # don't need particular variable name just need to loop twice 
        user_cards.append(deal_card())  # Deal two cards to the user  # if wanna add  only single item to the list, use append 
        computer_cards.append(deal_card()) # if we add multiple items to the list, use extend or + operator i.e. user_cards = user_cards + [deal_card(), deal_card()]

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card()) # Add another card to the user's hand
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17: # Computer must draw until score is 17 or higher even if it doesn't have a blackjack and user has passed
        # Computer draws cards until it reaches a score of 17 or higher
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()








# This code implements a simple command-line Blackjack game.