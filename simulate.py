from simulation import SIMULATION
import sys
import os

directOrGui = sys.argv[1]
solutionID = sys.argv[2]

simulate = SIMULATION(directOrGui, solutionID)

simulate.Run()
simulate.Get_Fitness()
simulate.Save_Sensor()
simulate.Save_Motor()