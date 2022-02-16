from random import randint
from fcOptimisation.utils import generateNewValue, binToInt


# Binary representation
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = []
        for _ in range(problParam['noDim']):
            gene = [randint(0,1) for _ in range(problParam['noBits'])] 
            self.__repres.append(gene)
        self.__fitness = 0.0
    
    @property
    def repres(self):
        # convert the binary matrix to a list of real values
        realRepres = []
        maxint = 2 ** self.__problParam['noBits']
        for gene in self.__repres:
            intValue = binToInt(gene)            
            realValue = self.__problParam['min'] + intValue / maxint * (self.__problParam['max'] - self.__problParam['min'])
            realRepres.append(realValue)
        return realRepres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        noBits = self.__problParam['noBits']
        newrepres = []
        for geneM, geneF in zip(self.__repres, c.__repres):
            cuttingPoint = randint(0, noBits - 1)
            newGene = [geneM[i] if i < cuttingPoint else geneF[i] for i in range(noBits)]
            newrepres.append(newGene)
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring
    
    def mutation(self):
        gene = randint(0, len(self.__repres) - 1)
        bit = randint(0, len(self.__repres[0]) - 1)
        self.__repres[gene][bit] = 1 - self.__repres[gene][bit]
        
    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
