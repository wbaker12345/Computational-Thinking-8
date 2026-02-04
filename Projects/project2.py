football_points = 0
basketball_points = 0
baseball_points = 0

answer1 = input("would your rather meet A lebron james, B patrick mahomes, C aaron judge? ")
if answer1 == "A" or answer1 == "a":
    basketball_points += 1
elif answer1 == "B":
    football_points += 1
elif answer1 == "C":
    baseball_points += 1

answer2 = input("do you watch more A football, basketball, C baseball? ")
if answer2 == "A":
    football_points += 2
elif answer2 == "B":
    basketball_points += 2
elif answer2 == "C":
    baseball_points += 2

answer3 = input("do you like A seahawks B sonics C mariners? ")
if answer3 == "A":
    football_points += 1
if answer3 == "B":
    basketball_points += 1
if answer3 == "C":
    baseball_points

answer4 = input("do you like A fast pace B mental C exsplosive type of games? ")
if answer4 == "A":
    basketball_points += 1
if answer4 == "B":
    baseball_points +=1
if answer4 == "C":
    football_points +=1
answer5 = input("what sport do you play the most A Basektball B Baseball C Football? ")
if answer4 == "A":
    basketball_points += 1
if answer4 == "B":
    baseball_points +=1
if answer4 == "C":
    football_points +=1

if basketball_points >= baseball_points and basketball_points >= football_points:
    print("you a basketball person")
if baseball_points >= football_points and baseball_points >= basketball_points:
    print(" you a baseball person")
if football_points >= basketball_points and football_points >= baseball_points:
    print("you are a football person")
