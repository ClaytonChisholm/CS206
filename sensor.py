import pybullet as p
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c



class SENSOR:
    def __init__(self, linkName):

        SENSOR.Prepare_To_Sense(self,linkName)
        self.test = "B"

    def Prepare_To_Sense(self,linkName):
        self.linkName = linkName
        values = np.zeros(1000)
        self.values = values



    def Get_Value(self,i):

        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) * np.sin(i * c.x)

    def Get_Value_2(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        #if i == 999:
         #   print(self.values)
    def Save_Values(self):

        np.save("data/"+str(self.linkName)+"Sensor_" + self.test, self.values)