import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

#pyrosim.Send_Cube(name="Box", pos=[0,0,.5] , size=[1,1,1])
#pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])

width = 1
height = 1
length = 1

for i in range(10):
    width = width * .9
    height = height * .9
    length = length * .9
    for j in range(5):
        for h in range(5):
            pyrosim.Send_Cube(name="Box", pos=[j, h, i + .5], size=[length, width, height])




pyrosim.End()