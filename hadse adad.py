import random

computer_number=random.randint(0,20) 

user_number=-1

while computer_number!=user_number:

    user_number=int(input())

    if computer_number==user_number:
        print("verygood")
      
    elif computer_number>user_number:
        print("up")

    elif computer_number<user_number:
        print("down")

    
