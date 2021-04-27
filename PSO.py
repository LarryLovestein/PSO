from AE import *
from dataclasses import dataclass



class Particula():
    def __init__(self,n):
        self.position=generateRandom(n)
        self.persBest=self.position
        self.viteza=[0]*n
        self.vecini=list()
    def __str__(self):
        return f"My position now {self.position}, my best Position {self.persBest}"
    def fitness(self):
        return fitness(self.position)
    def valBest(self):
        return fitness(self.persBest)

    def setPersBest(self):
        if fitness(self.position) < fitness(self.persBest):
            self.persBest=self.position
    def modificarePozitie(self):
        for i in range(len(self.position)):
            self.position[i]=self.position[i]+self.viteza[i]
    def getViteza(self,i):
        return self.viteza[i]

class Space():
    def __init__(self,popSize,n):
        self.popSize=popSize
        self.population=[Particula(n) for i in range(popSize)]
        self.gBest=self.population[0].position
    def valGbest(self):
        return self.gBest.fitness()
    def printSpace(self):
        for i in self.population:
            print(i)
    def setGBest(self):
        self.population.sort(key=lambda x: x.fitness(), reverse=False)
        self.gBest=self.population[0].position
    def getGlobalBest(self):
        return self.gBest

    def modificareViteza(self,c1,c2,w):

        for particle in self.population:
            for j in range(len(particle.viteza)):
                rand = random.random()
                val=(w*particle.viteza[j])+ (c1*rand)*(particle.persBest[j]-particle.position[j])+(c2*rand)*(self.gBest[j]-particle.position[j])
                if -5.12<val<5.12:
                    particle.viteza[j]=val
    def mediaPopulatiei(self):
        sum=0
        for i in self.population:
            sum+=i.fitness()
        return sum/len(self.population)

    def updatePopulatie(self):
        for particle in self.population:
           particle.setPersBest()
    def modificarePozitii(self):
        for i in self.population:
            i.modificarePozitie()

def PSO(c1,c2,w,popSize,n,maxIteration,nrRulari,racire):
    f = open("PSO.txt", "w")
    f.write("")
    f.close()
    j=0
    topRulari=list()
    while j< nrRulari:
        s=Space(popSize,n)
        i=0
        listCuValAvg=list()
        best=s.getGlobalBest()
        avg=s.mediaPopulatiei()
        listCuValAvg.append((float(fitness(best)),avg))
        wcopy=w
        while i < maxIteration:
            s.updatePopulatie()
            s.setGBest()
            s.modificareViteza(c1,c2,wcopy)
            s.modificarePozitii()
            avg = s.mediaPopulatiei()
            best=s.getGlobalBest()
            listCuValAvg.append((float(fitness(best)), avg))
            i+=1
            wcopy=wcopy*racire
        scrieVectorTuple("PSO.txt", listCuValAvg)
        j+=1

        topRulari.append(listCuValAvg[len(listCuValAvg)-1])
    return topRulari

#print(PSO(2.0,2.0,0.5,10,2,1000,10,0.999))







