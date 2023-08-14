import random
import pyfiglet
from termcolor import colored
r= colored(pyfiglet.figlet_format("rock , paper , scissor"),'yellow')
print(r)

while True:
    a= input("rock, paper , scissor...?")
    computer=["rock","paper","scissor"]
    com= random.choice(computer)
    print("entekhab computer:",com)
    if a==com:
        print("Aqaul")
    elif a=="rock":
      if com=="paper":
        print("computer won!")
      else:
        print("You won!")
    elif a=="paper":
        if com=="scissor":
            print("computer won!")
        else:
          print("You won!")
    elif a== "scissor":
        if com=="rock":
          print("computer won!")
    else:
        print("You mon!")

    again= input("play again? enter yes or No :")
    if again=="No":
       print ("bye")
       break