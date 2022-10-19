from random import random
import art
import game_data

def giveRandom():
    #his code will give random data of a account from game_data.py
    import random
    dataDict = game_data.data
    randomAccount = random.choice(dataDict)
    randAccName = randomAccount["name"]
    randAccDisc = randomAccount["description"]
    randAccContry = randomAccount["country"]
    randAccFollower = randomAccount["follower_count"]
    return f"{randAccName}, a {randAccDisc} lies in {randAccContry}" , randAccFollower

print(art.logo)
#initializing inital data for the first compare
lost = False
score = 0
firstAcc, firstAccFollower = giveRandom()
secondAcc, secondAccFollower = giveRandom()

while lost is False:

    print(f"Option A: {firstAcc}")
    print(art.vs)
    print(f"Option B: {secondAcc}")
    print("----------------------------------------------------------------------------------------------------------------------")
    userInput = str(input("Which would you think has more follower A or B: "))[0].upper()    
    
    if userInput == "A":
        if firstAccFollower > secondAccFollower:
            score += 1
            firstAcc, firstAccFollower = secondAcc, secondAccFollower
            secondAcc, secondAccFollower = giveRandom()
            print("----------------------------------------------------------------------------------------------------------------------")
            print("You are right")
            print("----------------------------------------------------------------------------------------------------------------------")
            continue #because right answer
        elif secondAccFollower > firstAccFollower:
            print("----------------------------------------------------------------------------------------------------------------------")
            print("you fail")
            print("----------------------------------------------------------------------------------------------------------------------")

            break #beause wrong answer and you lost
        
    elif userInput == "B":
        if secondAccFollower > firstAccFollower:
            score +=1
            secondAcc, secondAccFollower = giveRandom()
            print("----------------------------------------------------------------------------------------------------------------------")
            print("You are right")
            print("----------------------------------------------------------------------------------------------------------------------")

            continue #because the answer was right 
        elif firstAccFollower > secondAccFollower:
            print("----------------------------------------------------------------------------------------------------------------------")
            print("You are wrong")
            print("----------------------------------------------------------------------------------------------------------------------")

            break #because you are wrong
    else:
        print("I think it is your fault.")

print("your score is " + str(score))
print("program ends")