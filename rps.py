import random
 
items = ["rock", "paper", "scissor"]

# index = random.randint(0, 2)
# computer_choice = items[index]

computer_choice = random.choice(items)

print("0_rock")
print("1_paper")
print("2_scissor")
print("3_exit")
user_choice_index = int(input())
user_choice = items[user_choice_index]

computer_score = 0
user_score = 0

while True:

    if user_choice_index == "3":
        break

    if computer_choice == "rock" and user_choice == "scissor":
        print("computer wins")
        computer_score += 1

    elif computer_choice == "paper" and user_choice == "rock":
        print("computer wins")
        computer_score += 1

    elif computer_choice == "scissor" and user_choice == "paper":
        print("computer wins")
        computer_score += 1
        
    elif computer_choice == "scissor" and user_choice == "sissor":
        print("mosavi")

    elif computer_choice == "rock" and user_choice == "rock":
        print("mosavi")

    elif computer_choice == "paper" and user_choice == "paper":
        print("mosavi")

    elif computer_choice == "scissor" and user_choice == "rock":
        print("user wins")
        user_score += 1

    elif computer_choice == "rock" and user_choice == "paper":
        print("user wins")
        user_score += 1
        
    elif computer_choice == "paper" and user_choice == "scissor":
        print("user wins")
        user_score += 1