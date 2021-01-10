import csv
import matplotlib.pyplot as plt
with open("teste1.csv") as arquivo_csv: 
    leitor = csv.reader(arquivo_csv, delimiter=",") 
    numeros=[]
    nomes=[] 
    for coluna in leitor:
        numeros.append(int(coluna[0])) 
        nomes.append(coluna[1])       


    
    plt.plot(numeros, nomes)
    plt.show() 


    fig, ax = plt.subplots()
    ax.pie(numeros,labels=nomes,startangle=90,autopct='%d')
    plt.show()

    
    plt.bar(nomes,numeros)
    plt.show()

    