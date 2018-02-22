from random import randint

num = randint(0,100)

print("Guess # 1 [make sure it is an integer]: ")
guess = int(input()) 

i = 2
win = 0

while i <= 5:
    error = num-guess
    if error == 0:
        print("You win, your parents are proud")
        win = 1
        break
    elif error > 0:
        print("Higher")
    elif error < 0:
        print("Lower")
    print("Guess #",i," [make sure it is an integer]: ")    
    guess = int(input(""))
    i+=1
        
if win != 1:
    print("Sorry bruh, you lost")
