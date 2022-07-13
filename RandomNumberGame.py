line = "-----------------------------------------------------------"

import random
num = random.randint(1,100)

print(line + "\n" + "\t\tSelect Random Number" +"\n" + line)
name = input("Player Name: ")
player = None
turns = 0

while player != num:
    print(line)
    
    player = int(input("Enter Guess Number: "))
    if num == player:
        print("Wow! You selected the Correct Number")
    else:
        print("Wrong Number!")
        if player > num:
            print("Guess: Enter a Smaller Number!")
        else:
            print("Guess: Enter a Greater Number!")
    turns += 1

print(f"{line}\nYou Guessed Number in {turns} turns!")
    
with open("GameHighScore.txt","r") as f:
    content = f.read()
    high = ""
    for i in content:
        if i >= str(0) and i <= str(9):
            high += i
# print(high)

if turns < int(high):
    with open("GameHighScore.txt","w") as f:
        f.write(line + "\n" + "\t\tSelect Random Number" +"\n" + line + "\n")
        f.write("Name: " + name +"\n")
        f.write(line + "\n" + "Wow! You made High Score in " + str(turns) + " Turns!" + "\n" + line)
