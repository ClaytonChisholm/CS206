from solution import SOLUTION
import constants as c
import copy
import sys
import glob, os
import numpy

class PARALLELHILLCLIMBER:
    def __init__(self):

        self.currentGeneration = 0
        for f in glob.glob("*.nndf"):
            os.remove(f)
        for f in glob.glob("*.txt"):
            os.remove(f)
        self.nextAvailableID = 0
        self.parents = {}
        self.test = "B"

        #matrix
        p = c.populationSize
        g = c.numberOfGenerations + 1

        self.matrix = numpy.zeros((p, g))

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        #print(self.parents)

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGen in range(c.numberOfGenerations):
            print(currentGen)
            self.currentGeneration += 1
            self.Evolve_For_One_Generation()


        self.write()



        # current Generation loop
        #for currentGeneration in range(0, c.numberOfGenerations):
            #self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key].fitness = self.children[key].fitness

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        best = 5
        for key in self.parents:
            if self.parents[key].fitness < best:
                best_key = key
                best = self.parents[key].fitness
        print(self.parents[best_key].fitness)
        self.parents[best_key].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for bot in range(c.populationSize):
            solutions[bot].Start_Simulation("DIRECT")
        for bot in range(c.populationSize):
            solutions[bot].Wait_For_Simulation_To_End()

    def Print(self):
        for parent in self.parents:
            print('parent: ' + str(self.parents[parent].fitness) + ' child: ' + str(self.children[parent].fitness))


    def write(self):
        file = "AB/Fit_" + self.test + ".csv"
        numpy.savetxt(file, self.matrix, delimiter=',', fmt='%s')

        file2 = "AB/Fit_" + self.test + ".npy"
        numpy.save(file2, self.matrix)
        print(numpy.load(file2))

    def Print(self):
        for parent in self.parents:
            print('parent: ' + str(self.parents[parent].fitness) + ' child: ' + str(self.children[parent].fitness))
            self.matrix[self.parents[parent].myID % c.populationSize][self.currentGeneration] = self.parents[parent].fitness

