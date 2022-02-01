import pybullet as p
import time
import pybullet_data


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


for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)


p.disconnect()