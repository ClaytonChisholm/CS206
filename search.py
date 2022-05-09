import os
from parallelHillClimber import PARALLELHILLCLIMBER

#for i in range(0,5):
    #os.system("python generation.py")
    #os.system("python simulate.py")

phc = PARALLELHILLCLIMBER()
#phc.Show_Best()
phc.Evolve()
phc.Show_Best()