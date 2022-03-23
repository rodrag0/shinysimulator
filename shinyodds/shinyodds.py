
# seed the pseudorandom number generator
from random import seed
from random import random
from random import randint

#define count
# seed random number generator
rango=int(input("How many times do you want your simulation to run?: "))
oddsholder=int(input("enter odds of shiny pokemon for default shiny odds type 0: "))
odds=int(oddsholder)
if oddsholder!=0:
    odds=oddsholder

elif oddsholder == 0:
    odds=4096
#seed(random()*oddsholder) #apparently outdated
newodds=odds-1
print("odds", odds)
ntoget=int(randint(0,newodds))
n=int(randint(0, newodds))
count=0
countsum=0
#rango=int(10)
# generate some random numbers
##if n==ntoget:
##    print("n equals ntoget")
while n==ntoget:
    n=randint(0, newodds)
if oddsholder!=0:
    odds=oddsholder

elif oddsholder == 0:
    odds=4096
print("odds son:", odds)
print("factores son n, ntoget", n, ntoget)
for x in range(rango):
    while n != ntoget:   #ntoget es el numero que debe salir para concluir la ronda, es decir es cuantas veces tardo en salir ese numero con probablidad 1/odds
        n=randint(0,odds)
        count+=1
        print(n)
        #print(count)
    
    print("FINISHED", x+1 ,"TIMES")
    print("count was", count)
    countsum=count+countsum
    count=0
    while n==ntoget:
        n=randint(0, newodds)  
n=1
if n==1:
    average=countsum/rango
    print("average in ",rango," times was", average)


    