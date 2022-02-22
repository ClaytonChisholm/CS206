import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random




print('works')
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


#gravity
p.setGravity(0,0,-9.8)

#add floor
planeId = p.loadURDF("plane.urdf")

#load box
p.loadSDF("world.sdf")

#robot id
robotId = p.loadURDF("body.urdf")

#prepare
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles  = numpy.linspace(0, 2*numpy.pi, 1000)
targetAnglesF = []
targetAnglesB = []

Famplitude = numpy.pi/4
Ffrequency = 20
FphaseOffset = numpy.pi/2


Bamplitude = numpy.pi/4
Bfrequency = 20
BphaseOffset = 0

#for loop
for i in range(0, 1000):

    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    targetAnglesF.append(Famplitude * numpy.sin(targetAngles[i] * Ffrequency + FphaseOffset) * numpy.pi/4)
    targetAnglesB.append(Bamplitude * numpy.sin(targetAngles[i] * Bfrequency + BphaseOffset) * numpy.pi/4)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAnglesF[i],
    maxForce = 50)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAnglesB[i],
    maxForce = 50)

    time.sleep(1/60)

#save data
numpy.save("data/dataBackLeg.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/datafrontLeg.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)
print(backLegSensorValues)

p.disconnect()
