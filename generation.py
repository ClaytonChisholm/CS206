import pyrosim.pyrosim as pyrosim



def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[5, 5, .5], size=[1, 1, 1])
    # pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])
    pyrosim.End()


def Create_Robot():

    pyrosim.Start_URDF("body.urdf")
    #torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    #front leg
    pyrosim.Send_Joint(name="Torso_front_Leg", parent="Torso", child="front_Leg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="front_Leg", pos=[.5, 0, -.5], size=[1, 1, 1])
    #back leg
    pyrosim.Send_Joint(name="torso_back_Leg", parent="Torso", child="back_leg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="back_leg", pos=[-.5, 0, -.5], size=[1, 1, 1])
    pyrosim.End()



Create_World()
Create_Robot()