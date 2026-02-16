import random
from art import logo


# Return a random card value (Ace starts as 11).
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Compute score, handling blackjack and Ace reduction.
def calculate_score(cards):
        score = sum(cards)
        if score == 21 and len(cards) == 2:
            return 0
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    # Initial deal: two cards each.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(computer_cards[0])
    computer_score = calculate_score(computer_cards)
    is_game_over = False
    while not is_game_over:
        current_score = calculate_score(user_cards)
        print(f"This is your current score {current_score}")
        if current_score == 0 or current_score > 21:
            is_game_over = True
        else:
            user_request = input("Do you want to draw another card y for yes n for no: ").lower()
            if user_request == "y":
                user_cards.append(deal_card())
            if user_request == "n":
                is_game_over = True
    # Dealer draws until 17 or blackjack.
    if current_score != 0 and current_score <= 21:
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    if current_score > 21:
        print(f"You Lose your score is:{current_score}")
    elif current_score == 0 and computer_score == 0:
        print("A tied BlackJack:)")
    elif current_score == 0:
        print("Black Jack You Win")
    elif computer_score > 21:
        print(f"You Win the Computers score was {computer_score}")
    elif computer_score == 0:
        print("Computer Wins")
    elif computer_score == current_score:
        print("Tie")
    elif computer_score > current_score:
        print(f"You lose the computer had {computer_score} > {current_score}")
    else:
        print(f"You Win the User had {current_score} > {computer_score}")
    print(f"The User had {user_cards} and the computer had {computer_cards}")

# Main replay loop.
while input("Would You like to play Again y for yes n for no: ") == "y":
    print("\n" * 20)
    play_game()


