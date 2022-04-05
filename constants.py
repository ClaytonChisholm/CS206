import numpy
import math

Famplitude = numpy.pi/4
Ffrequency = 20
FphaseOffset = numpy.pi/2

Bamplitude = numpy.pi/4
Bfrequency = 20
BphaseOffset = 0

maxForce = 50

twoPi = 2*numpy.pi

loopLow = 0
loopHigh = 1000

targetAnglesLow = 0
targetAnglesHigh = 1000

gravity = -9.8
zero = 0

FPS = 1/30

LegSensorValues = 1000

amplitudeTorso_BackLeg = math.pi/4.0
frequencyTorso_BackLeg = 1/10.0
offsetTorso_BackLeg = 0

amplitudeFrontLeg_Torso = math.pi/4.0
frequencyFrontLeg_Torso = 1/20.0
offsetFrontLeg_Torso = 0

numberOfGenerations = 10

populationSize = 10

numSensorNeurons = 9


numMotorNeurons = 8

sensors = numpy.arange(numSensorNeurons)
motors = numpy.arange(numSensorNeurons,numMotorNeurons)

motorJoinRange = 0.5