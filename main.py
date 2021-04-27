from UI import *
import matplotlib.pyplot as plt
import random
import time
from PSO import *
from AE import *
def principal():
    while True:
        afisareMeniu()
        x = input("Introdu numarul corespunzaotr: ")
        if(x == "1"):

            populationNR = int(input("population number:"))
            n = int(input("Dimensiunea(n):"))
            k = int(input("cate elemente random pentru turnir se aleg"))
            nrGeneratii = int(input("Cate generatii sa fie:"))
            nrRulari = int(input("Cate rulari:"))
            alpha = float(input("Alpha:"))
            parentSel="turnir"
            start_time = time.time()
            topRulari = list(evolutionaryAlg(populationNR, n,nrGeneratii,nrRulari,k,alpha,parentSel))
            print("--- %s seconds ---" % (time.time() - start_time))
            i = topRulari.index(valMinima(topRulari))
            vect = citesteVectorTuple("REAL.txt", i)
            print(topRulari[i])
            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. 4 " )
            plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()

        if(x=="2"):

            populationNR = int(input("population number:"))
            n = int(input("Dimensiunea(n):"))
            k = int(input("cate elemente random pentru turnir se aleg"))
            nrGeneratii = int(input("Cate generatii sa fie:"))
            nrRulari = int(input("Cate rulari:"))
            pb = float(input("Probabilitatea:"))
            parentSel = "rank"
            start_time = time.time()
            topRulari = list(evolutionaryAlg2(populationNR, n,nrGeneratii,nrRulari,k,pb,parentSel))
            print("--- %s seconds ---" % (time.time() - start_time))
            i = topRulari.index(valMinima(topRulari))
            vect = citesteVectorTuple("REAL.txt", i)
            print(topRulari[i])
            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. 4 " )
            plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()
        if x=="3":
            populationNR = int(input("population number:"))
            n = int(input("Dimensiunea(n):"))
            maxIteration = int(input("Nr maxim iteratii:"))
            nrRulari = int(input("Cate rulari:"))
            c1 = float(input("c1:"))
            c2 = float(input("c2:"))
            w = float(input("w:"))
            racire=float(input("Factor racire:"))
            start_time = time.time()
            topRulari = list(PSO(c1,c2,w,populationNR,n,maxIteration,nrRulari,racire))
            print("--- %s seconds ---" % (time.time() - start_time))
            i = topRulari.index(valMinima(topRulari))
            vect = citesteVectorTuple("PSO.txt", i)
            print(topRulari)
            print(i)
            print(topRulari[i])
            print(vect)
            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB.4(PSO) ")
            #plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()
        if x=="4":

            pop=generatePopulation(3,2)
            print("FITNESS POP")
            for i in pop:
                print(fitness(i))
            bestP=rankSelection(pop)
            print("FITNESS BEST")
            for i in bestP:
                print(fitness(i))




        if (x == "0"):
            print("codul s-a terminat cu succes")

principal()


