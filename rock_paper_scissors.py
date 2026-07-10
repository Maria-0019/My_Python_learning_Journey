import random

# choices
choices = ["stone", "paper", "scissors"]

# score
user_score = 0
computer_score = 0

print(" Welcome to Stone Paper Scissors Game!")
print("Type 'exit' to quit\n")

while True:
    user = input("Enter stone / paper / scissors: ").lower()

    if user == "exit":
        print("\n Game Over!")
        print(f"Final Score → You: {user_score} | Computer: {computer_score}")
    if user not in choices:
        print("Invalid choice, try again!\n")
        continue

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    # game logic
    if user == computer:
        print(" It's a tie!")
   
   elif (
        (user == "stone" and computer == "scissors") or
        (user == "paper" and computer == "stone") or
        (user == "scissors" and computer == "paper")
    ):
        print(" You win!")
        user_score += 1

    else:
        print(" Computer wins!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}\n")


