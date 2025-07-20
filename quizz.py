print("Welcome to our quiz programm")

playing = input("do you want to play? :")
if playing.lower() != "yes" :
    quit()
print("Okay let's begin this quiz :) !")

score = 0

answer = input("Smallest country in the world? :")
if answer.lower() == "vatican" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("What is the name of naruto's signature jutsu? :")
if answer.lower() == "rasengan" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("who was the fourth hokage of the Hidden Leaf Village? :")
if answer.lower() == "minato" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("which country is famous for the Eiffel tower? :")
if answer.lower() == "france" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("which is the largest Ocean in the world? :")
if answer.lower() == "pacific ocean" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("what is the capital of japan? :")
if answer.lower() == "tokyo" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("which indian state is know as the spices garden of india? :")
if answer.lower() == "kerala" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("which state has the highest population in India? :")
if answer.lower() == "uttar pradesh" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("which of the following is not a Rabi crop? a) Wheat b) Barlet c) Mustard d) paddy : ")
if answer.lower() == "paddy" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

answer = input("largest state in india by area? :")
if answer.lower() == "vatican" :
    print("Correct!")
    score += 1
else :
    print("Oops Incorrect!")

print("You got" + str(score) + "questions correct !")
print("You got" + str((score/10) * 100) + "%.")


