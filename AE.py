import numpy as np
from UI import scrieVectorTuple



def fitness(x):
    value=0;
    for i in range(len(x)):
        value=value+5*(i+1)*(x[i] ** 2)
    return value

def generateRandom(n):
    x=np.random.uniform(-5.12, 5.12, n)
    return x

def generatePopulation(popSize,n):
    population=list()
    i=0
    while i<popSize:
        population.append(list(generateRandom(n)))
        i+=1
    return population

import random
'''
se alege un punct random si de la punctul respectiv si modifica din fiecare vector valoarea
'''
def incrConvSimpla(parent1,parent2,alpha):
    point=random.randint(0,len(parent1))
    kid1=parent1.copy()
    kid2=parent2.copy()
    for i in range(point,len(parent1)):
        kid1[i]=alpha*parent2[i]+(1-alpha)*parent1[i]
        kid2[i]=alpha*parent2[i]+(1-alpha)*parent1[i]
    return kid1,kid2

def incrCont(parent1,parent2,pb):
    kid1 = parent1.copy()
    kid2 = parent2.copy()
    for i in range(0,len(parent1),2):
        if(random.uniform(0,1)<pb):
            kid1[i]=(parent1[i]+parent2[i+1])/2
            kid2[i]=(parent1[i]+parent2[i+1])/2
    return kid1,kid2

def parentsCrossoverSimple(parents,alpha):
    kids=list()
    for i in range(0,len(parents),2):
        kid1,kid2=incrConvSimpla(parents[i],parents[i+1],alpha)
        kids.append(kid1)
        kids.append(kid2)
    return kids

def parentsCrossoverCont(parents,pb):
    kids=list()
    for i in range(0,len(parents),2):
        kid1,kid2=incrCont(parents[i],parents[i+1],pb)
        kids.append(kid1)
        kids.append(kid2)
    return kids

def uniformMutation(kid):
    point = random.randint(0, len(kid)-1)
    kid[point]=np.random.uniform(-5.12, 5.12)
    return kid

def mutationKids(kids):
    mutated=kids.copy()
    n = len(mutated)
    i = 0
    while i < n:
        copiemutated = mutated[i].copy()
        m = uniformMutation(copiemutated)
        mutated[i] = m.copy()
        i += 1
    return mutated


def turnirSelection(population,k):
    i=0
    bestParents=list()
    while i <len(population):
        poz = np.random.default_rng().choice(len(population), size=k, replace=False)
        bestParent = population[poz[0]]
        for j in poz:
            if fitness(population[j]) < fitness(bestParent):
                bestParent=population[j].copy()
        bestParents.append(bestParent)
        i += 1
    return bestParents


def rankSelection(population):
    listPb=list()
    bestParents=list()
    population.sort(key=lambda x: fitness(x), reverse=True)
    prevPb=0.0
    s=1.5
    for i in population:
        pb=(2-s)/(len(population))+2*((population.index(i))*(s-1))/(len(population)*(len(population)-1))
        #pb = ((2 - s)  + 2 * ((population.index(i)) * (s - 1)) / ((len(population) - 1)))/len(population)

        listPb.append((prevPb,pb+prevPb))
        prevPb=pb+prevPb

    while len(bestParents)<len(population):
        pb=random.uniform(0,1)
        for j in listPb:
            if pb>=j[0] and pb<j[1]:
                bestParents.append(population[listPb.index(j)])
                break
    return bestParents



def sortAllPeople(allPeople):
    allPeople.sort(key=lambda x: fitness(x), reverse=False)
    return allPeople



def selectSurvivors(allPeople,populationNR): # din lista tuturor persoanelor din generatie care sunt sortati
    bestOfAll=list()
    n=int(0.1*len(allPeople))
    for i in range(n):
        bestOfAll.append(allPeople[i]) #se salveaza 10% din cei mai buni si se elimina dupa
    allPeople=allPeople[n:]
    selectiaTurnir=turnirSelection(allPeople,3)
    for i in range(len(bestOfAll),populationNR):
        bestOfAll.append(selectiaTurnir[i])
    return bestOfAll

def bestAvgPopulation(population):
    suma=0
    bestOne=sortAllPeople(population)[0]
    for i in population:
        suma+=fitness(i)
    return bestOne,suma/len(population)

#print(bestAvgPopulation([[1,2,3,4],[1,2,3,4],[0,0,0,1],[1,2,3,4]]))
import operator

def valMinima(lista):
    copie=lista.copy()
    copie.sort(key=operator.itemgetter(0))
    return copie[0]

def evolutionaryAlg(populationNR, n,nrGeneratii,nrRulari,k,alpha,parentSel):
    f = open("REAL.txt", "w")
    f.write("")
    f.close()
    i=0
    toateRularile=list()
    while i<nrRulari:
        populatie=generatePopulation(populationNR,n)
        listaCuValAVG=list()
        bestOne,avg=bestAvgPopulation(populatie)
        listaCuValAVG.append((float(fitness(bestOne)),avg))
        t=1
        while t < nrGeneratii:
            if parentSel=="turnir":
                parents=turnirSelection(populatie,k) #se selecteaza parintii
            elif parentSel=="rank":
                parents=rankSelection(populatie)
            kids=parentsCrossoverSimple(parents,alpha) #se genereaza copii
            kidsM=mutationKids(kids)# se fac mutatile la copii
            allPeople=parents+kids+kidsM    #se formeaza o noua populatie
            allPeople=sortAllPeople(allPeople) # se sorteaza dupa fitness
            populatie=selectSurvivors(allPeople,populationNR) #se face selectia populatiei
            bestOne, avg = bestAvgPopulation(populatie) #se determina cel mai bun individ din populatie si avg
            listaCuValAVG.append( (float(fitness(bestOne)), avg))    #se adauga in vectorul specific pe care il scriu in fisier
            t+=1#Creste numarul de generatii

            #print(listaCuValAVG)
        scrieVectorTuple("REAL.txt",listaCuValAVG)#scriem intr-un fisier vectorul de best/avg pentru fiecare generatie pentru plot
        #adaugam in toateRularile bestul si Avg ultimei populatii pentru a putea determina bestul din n rulari
        toateRularile.append(listaCuValAVG[len(listaCuValAVG)-1])
        i+=1
    return toateRularile



def evolutionaryAlg2(populationNR, n,nrGeneratii,nrRulari,k,pb,parentSel):
    f = open("REAL.txt", "w")
    f.write("")
    f.close()
    i=0
    toateRularile=list()
    while i<nrRulari:
        populatie=generatePopulation(populationNR,n)
        listaCuValAVG=list()
        bestOne,avg=bestAvgPopulation(populatie)
        listaCuValAVG.append((float(fitness(bestOne)),avg))
        t=1
        cpb=pb
        while t < nrGeneratii:
            if parentSel == "turnir":
                parents = turnirSelection(populatie, k)  # se selecteaza parintii
            elif parentSel == "rank":
                parents = rankSelection(populatie)
            kids=parentsCrossoverCont(parents,cpb) #se genereaza copii
            kidsM=mutationKids(kids)# se fac mutatile la copii
            allPeople=parents+kids+kidsM    #se formeaza o noua populatie
            allPeople=sortAllPeople(allPeople) # se sorteaza dupa fitness
            populatie=selectSurvivors(allPeople,populationNR) #se face selectia populatiei
            bestOne, avg = bestAvgPopulation(populatie) #se determina cel mai bun individ din populatie si avg
            listaCuValAVG.append( (float(fitness(bestOne)), avg))    #se adauga in vectorul specific pe care il scriu in fisier
            t+=1#Creste numarul de generatii
            cpb=0.999*cpb
            #print(listaCuValAVG)
        scrieVectorTuple("REAL.txt",listaCuValAVG)#scriem intr-un fisier vectorul de best/avg pentru fiecare generatie pentru plot
        #adaugam in toateRularile bestul si Avg ultimei populatii pentru a putea determina bestul din n rulari
        toateRularile.append(listaCuValAVG[len(listaCuValAVG)-1])
        i+=1
    return toateRularile