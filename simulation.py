import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

import numpy
import random



from world import WORLD
from robot import ROBOT


class SIMULATION:
    # Constructor
    def __init__(self, directOrGui, solutionID):
        self.solutionID = solutionID
        self.directOrGui = directOrGui
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -50)

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

    def Run(self):
        for i in range(300):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Prepare_To_Act()
            self.robot.Act(i)
            '''
            self.backLegJointValues[i] = backLegPosition
            self.frontLegJointValues[i] = frontLegPosition
            '''
            #t.sleep(1. / 480.)
            t.sleep(1./60.)
    def Save_Sensor(self):
        self.robot.Save_Sensor()
    def Save_Motor(self):
        self.robot.Save_Motor()

    def Get_Fitness(self):
        self.robot.Get_Fitness()



    def __del__(self):
        p.disconnect()
