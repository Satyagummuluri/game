import random

# Define options
options = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

# Validate user input
if user_choice not in options:
    print("Invalid choice. Please try again.")
    exit()

# Computer's choice
computer_choice = random.choice(options)

# Print choices
print(f"\nYou chose: {user_choice.capitalize()}")
print(f"Computer chose: {computer_choice.capitalize()}")

# Determine winner
if user_choice == computer_choice:
    print("\nIt's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("\nYou win!")
else:
    print("\nYou lose!")
