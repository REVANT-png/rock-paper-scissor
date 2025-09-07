import random
c = random.randint(0,2)
print("hello user welcome to the game")
print("rule are simple rocks cuts scissor scissor cuts paper and aper covers rock")
print("so press 0 for rock , 1 for paper and  2 for scissor")

d  = int(input(" "))
if d==0:
    print("you chose rock")
elif d==1:
    print("you chose paper")
elif d==2:
    print("you chose scissor")

if c==0:
    print("computer chose rock")
elif c==1:
    print("computer chose paper")
elif c==2:
    print("computer chose scissor")

if   c ==0 and  d==0:
    print(" thats a draw ")
elif c ==1 and  d==1:
    print(" thats a draw ")
elif c ==2 and  d==2:
    print(" thats a draw ")
elif c==0 and d==1 :
    print("you won as paper covers rock")
elif c ==0 and  d==2:
    print(" you lost as rock beats scissor ")
elif c ==1 and  d==0:
    print("you lost as paper covers rock")

elif c ==1 and  d==2:
    print(" you won as scissor cuts paper ")
elif c ==2 and  d==0:
    print(" you won as rock beats scissor ")
elif c ==2 and  d==1:
    print(" you lost as scissor cuts paper ")