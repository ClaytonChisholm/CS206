from solution import SOLUTION
import constants as c
import copy
import sys
import glob, os

class PARALLELHILLCLIMBER:
    def __init__(self):

        for f in glob.glob("*.nndf"):
            os.remove(f)
        for f in glob.glob("*.txt"):
            os.remove(f)

        self.nextAvailableID = 0
        self.parents = {}

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        #print(self.parents)

    def Evolve(self):
        self.parent.Evaluate()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            pass

    def Evolve(self):
        #directOrGui = sys.argv[1]
        for i in range(0, c.populationSize):
            self.parents[i].Start_Simulation("DIRECT")
        for i in range(0, c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()

        # current Generation loop
        #for currentGeneration in range(0, c.numberOfGenerations):
            #self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print("\n")
        self.Print()
        print("\n")
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_Id(self.nextAvalibleID)
            self.nextAvalibleID += 1


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
        for key in self.parents:
            print("Parent Fitness " + str(self.parents[key].fitness) + " Child Fitness " + str(
                self.children[key].fitness))