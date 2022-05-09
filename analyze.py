import numpy
import matplotlib.pyplot


A = numpy.load("data/BackLeg2Sensor_A.npy")

matplotlib.pyplot.plot(A, linewidth = 2)

B = numpy.load("data/BackLeg2Sensor_B.npy")

matplotlib.pyplot.plot(B, linewidth = 1)

matplotlib.pyplot.legend(("backLegSensorA", "backLegSensorB"))
matplotlib.pyplot.show()