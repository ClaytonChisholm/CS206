from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]

simulate = SIMULATION(directOrGui)

simulate.Run()

simulate.Save_Sensor()
simulate.Save_Motor()
simulate.Get_Fitness()