import random
score=0
count=0
while count<5:
    correct = random.choice(['r','p','s'])
    print("Guess Rock(r),Paper(p) and Sciccor(s)..")
    guess = input()
    if guess == correct:
        print("DRAWW..!!")
    elif guess=='r' and correct=='s':
        print("Hurray..!!You Won..")
        score +=1
    elif guess=='s' and correct=='p':
        print("Hurray..!!You Won..")
        score +=1
    elif guess=='p' and correct=='r':
        print("Hurray..!!You Won..")
        score +=1
    elif guess=='r' and correct=='p':
        print("Better Luck Next Time..@")
    elif guess=='s' and correct=='r':
        print("Better Luck Next Time..@")
    elif guess=='p' and correct=='s':
        print("Better Luck Next Time..@")
    else:
        print("Choose Wisely..!! You got Minus Score")
        score-=1
    count+=1
score = score*20
print("\nYour score is.."+str(score)+"..!!")