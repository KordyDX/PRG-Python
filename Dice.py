import random
#declaring two sets of dices and their values mate
dice1, dice2 = random.randint(1,6), random.randint(1,6)
CPUdice1, CPUdice2 = random.randint(1,6), random.randint(1,6)
print("//You rolled %d and %d" %(dice1, dice2))
print("//The CPU rolled %d and %d\n" %(CPUdice1, CPUdice2))
#now ima proper mix em up ye
score = dice1 + dice2
CPUscore = CPUdice1 + CPUdice2
#this move cost me 5 quid m8 im broke af
print("//Your total score is %d" %score)
print("//The CPU's score is %d\n" %CPUscore)
#now im gonna dissapoint you in life by smuggling 2.57299mg of pure uranium into a kindergarten help i need therapy
if(score > CPUscore):
    print("//You win by " + str(score - CPUscore) + " points.")
elif(score < CPUscore):
    print("//The computer won by " + str(CPUscore - score) + " points.")
elif(score == CPUscore):
    print("//It's a draw. No winner.")
