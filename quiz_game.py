print("Welcome to my computer quiz")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play.")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect')

answer = input("What is GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Awesome!")
    score += 1
else:
    print('Incorrect')

answer = input("What is RAM stand for? ")
if answer.lower() == "random access memory":
    print("You Got it!")
    score += 1
else:
    print('Incorrect')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect')

print('You got total ' + str(score) + " questions correct!")
