import random
z = int(input("Digite quantos jogos você deseja fazer:"))
x=[]
cont=0
while cont<z:
    x = random.sample(range(1,60),6)
    x.sort()
    print(x)    
    cont+=1
    
