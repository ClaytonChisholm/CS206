import matplotlib
import numpy as numpy
import matplotlib.pyplot as plt

# get values
valuesA = numpy.load("AB/Fit_A.npy")
valuesB = numpy.load("AB/Fit_B.npy")

# get rows of matrix (A and B will have same shape)
rows = valuesA.shape[0]
cols = valuesA.shape[1]

x = []
for i in range(0, cols):
    x.append(i)
# code for plotting all runs at each generation
'''
for i in range(0, rows):
    labelA = "Bot A, Gen:" + str(i)
    labelB = "Bot B, Gen:" + str(i)

    plt.plot(x, valuesB[i,:], label = labelB, linewidth = 3, color='blue')
    plt.plot(x, valuesA[i, :], label=labelA, linewidth=1, color='red')
    plt.xlim(1, 10)

plt.legend(loc=(1.04,0))
plt.show()

'''

valuesA = numpy.load("AB/Fit_A.npy")
valuesB = numpy.load("AB/Fit_B.npy")

plt.plot(numpy.mean(valuesA, axis=0), linewidth=2, color=(0, 1, 0))
plt.plot(numpy.mean(valuesB, axis=0), linewidth=2, color=(0, 0, 1))
plt.xlim(1, 50)
plt.legend(("CPG", 'no CPG'))


plt.show()
#motor

#backLegSensorData = numpy.load("data/dataBackLeg.npy")

#matplotlib.pyplot.plot(backLegSensorData, linewidth = 2)

#frontLegSensorData = numpy.load("data/dataFrontLeg.npy")

#matplotlib.pyplot.plot(frontLegSensorData, linewidth = 1)

#matplotlib.pyplot.legend(("backLeg", "frontLeg"))
#matplotlib.pyplot.show()

#Average

#labelA = "Bot A, Gen:" + str(i)
#labelB = "Bot B, Gen:" + str(i)
#plt.plot(numpy.mean(valuesA[i]), label = labelB, linewidth = 3, color='blue')
#plt.plot(numpy.mean(valuesB[i]), label= labelA, linewidth=1, color='red')
#plt.xlim(1, 10)

#plt.show()