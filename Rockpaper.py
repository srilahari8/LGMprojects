import random
rock="🤜"
paper="🫱"
scissors="✌"
game_images=[rock,paper,scissors]
def running(): 
 user_choice=int(input("enter your choice: type 0 for Rock,1 for paper ,2 for Scissors."))
 if user_choice >= 3 or user_choice <0:
    print(" you entered invalid number, You lose.")
 else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2) 
    print("computer choose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("Its draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif computer_choice==2 and user_choice==0:
        print("you win")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    play=input("Do you want to play again type(y) for yes ").lower()
    if play=='y':
       running()
running()
