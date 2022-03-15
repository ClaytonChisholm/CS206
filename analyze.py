import numpy
import matplotlib.pyplot


backLegSensorData = numpy.load("data/dataBackLeg.npy")

matplotlib.pyplot.plot(backLegSensorData, linewidth = 2)

frontLegSensorData = numpy.load("data/dataFrontLeg.npy")

matplotlib.pyplot.plot(frontLegSensorData, linewidth = 1)

matplotlib.pyplot.legend(("backLeg", "frontLeg"))
matplotlib.pyplot.show()