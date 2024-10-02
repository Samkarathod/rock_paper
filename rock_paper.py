import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        return "Invalid choice!"

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lose!"

    # Display the result
    return f"User choice: {user_choice}\nComputer choice: {computer_choice}\nResult: {result}"

print(rock_paper_scissors())