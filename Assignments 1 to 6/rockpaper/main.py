import random
def computer_choice():
    return random.choice(['rock','paper','scissor'])
def game(player,Computer):
    if player==Computer:
        return "Its a tie !!"
    if (player=='rock' and Computer=='paper') or (player=='paper' and Computer=='scissor') or (player=='scissor' and Computer=='rock'):
        return "Computer wins"
        return "player wins"
while True:  
    print("Welcome to the game ,type Exits to get out of this game ! Thankyou")
    player_choice=input("Enter your choice from {rock,paper,scissor} : " ).lower()  
    if player_choice=='exit':
         print("GoodBye!")
         break
    elif player_choice not in ['rock','paper','scissor']:
        print("Invalid choice ! Try again ..")
        continue
    computer=computer_choice()
    print("Computer chose : " ,computer)
    result = game(player_choice,computer)
    print(result)
