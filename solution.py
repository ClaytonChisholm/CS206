import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time as t
import constants as c
import numpy as np

class SOLUTION:

    def __init__(self, ID):
        self.myID = ID
        self.weights = np.zeros((c.numSensorNeurons, c.numMotorNeurons))

        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                self.weights[i][j] = np.random.rand() * 2 - 1

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Brain()
        self.Generate_Body()

        print("start /B python simulate.py " + directOrGui + " " + str(self.myID))
        os.system("start /B python simulate.py " + directOrGui +  " " + str(self.myID))
        pass

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            t.sleep(0.01)
        while True:
            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                self.fitness = float(f.readline())
                break
            except Exception:
                print("waiting")
                t.sleep(0.01)

        f.close()
        os.remove("fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[5, 5, .5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])
        pyrosim.End()

    def Evaluate(self, directOrGui):
        pass

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        #TORSO/UPPER LEGS

        # LINK: TORSO (abs)
        length, width, height = 1, 1, 1
        x, y, z = 0, 0, 1
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

        #BACK LEG

        # JOINT: TORSO - Backleg (abs)
        x, y, z = 0, -0.5, 1
        pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[x, y, z], jointAxis = "1 0 0")

        # LINK: Backleg (rel)
        length, width, height = 0.2, 1, 0.2
        x, y, z = 0.,-.5,0.
        pyrosim.Send_Cube(name="Backleg", pos=[x, y, z], size=[length, width, height])

        #FRONT LEG

        # JOINT: TORSO - Frontleg (abs)
        x, y, z = 0, 0.5, 1
        pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[x, y, z], jointAxis = "1 0 0")

        # LINK: Frontleg (rel)
        length, width, height = 0.2, 1, 0.2
        x, y, z = 0, 0.5, 0
        pyrosim.Send_Cube(name="Frontleg", pos=[x, y, z], size=[length, width, height])

        #LEFT LEG

        # JOINT: TORSO - LeftLeg (abs)
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[0.5, 0., 1.], jointAxis="0 1 0")
        # LINK: Frontleg (rel)
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0., 0.], size=[1., 0.2, 0.2])

        # RIGHT LEG

        # JOINT: TORSO - LeftLeg (abs)
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[-.5, 0., 1.], jointAxis="0 1 0")
        # LINK: Frontleg (rel)
        pyrosim.Send_Cube(name="RightLeg", pos=[-.5, 0., 0.], size=[1., 0.2, 0.2])

        # LOWER LEGS

        # front lower
        pyrosim.Send_Joint(name="FrontLeg_FrontLeg2", parent="Frontleg", child="FrontLeg2", type="revolute",
                           position=[0., 1, 0.], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        # back lower
        pyrosim.Send_Joint(name="BackLeg_BackLeg2", parent="Backleg", child="BackLeg2", type="revolute",
                           position=[0., -1., 0.], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        # left lower
        pyrosim.Send_Joint(name="LeftLeg_LeftLeg2", parent="LeftLeg", child="LeftLeg2", type="revolute",
                           position=[1., 0., 0.], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        # right lower
        pyrosim.Send_Joint(name="RightLeg_RightLeg2", parent="RightLeg", child="RightLeg2", type="revolute",
                           position=[-1., 0, 0.], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])


        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID) + ".nndf")
        # SENSORS

        # Torso
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # Backleg
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Backleg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg2")
        # frontLeg
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Frontleg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLeg2")
        # leftLeg
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLeg2")
        # right leg
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLeg2")

        # MOTORS
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_Backleg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_Frontleg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLeg2")

        for currentRow in range(c.numSensorNeurons):
            # iterate over motor neurons
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        chosenRow = random.randint(0, c.numSensorNeurons - 1)
        chosenColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[chosenRow, chosenColumn] = random.random() * 2 - 1

    def Set_ID(self, Id):
        self.myID = Id