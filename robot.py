import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("Body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.remove("brain" + str(self.solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for j in self.sensors:
            self.sensors[j].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle, i)
                #print(neuronName, jointName, desiredAngle)

    def Save_Sensor(self):
        for j in self.sensors:
            self.sensors[j].Save_Values()

    def Save_Motor(self):
        for j in self.motors:
            self.motors[j].Save_Values()
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        fitnessFile = open("fitness"+str(self.solutionID) + ".txt", "w")
        fitnessFile.write(str(xCoordinateOfLinkZero))
        fitnessFile.close()
