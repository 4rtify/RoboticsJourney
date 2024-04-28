# pip3 install roboticstoolbox-python

# For some reason I had to update the following file:
# 
# \roboticstoolbox\mobile\EKF.py line 9
# 
# From:
#     from scipy import integrate, randn
# To: 
#     from scipy import integrate #, randn
#     from numpy.random import randn

# Personal Notes Below:
#   Thumb 
#       Z - Yaw - "theta" - aligning to Xi-1 to Xi 
#       Z - Distance - "D" - the displacement along the Z axis - from Di-1 to Di
#   Pointer finger
#       X - Roll - "a" - displacement along the X axis - AKA "r" or radius
# 	    "Alpha" - X - Pitch
#   Middle Finger 
#       Y - Pitch
# Transformation Matrix - Sub-Translation / Sub-Rotation matrix

# TODO / review
# What is the link off set?
# What is the common normal?
    # https://www.youtube.com/watch?v=rA9tm0gTln8&ab_channel=TekkotsuRobotics


import math
import roboticstoolbox as rtb
import numpy as np

def getDHMatrix(theta: float, d: float, a: float, alpha: float) -> np.array:
    theta = math.radians(theta)
    alpha = math.radians(alpha)
    return np.array([
        [np.cos(theta), -1*np.sin(theta)*np.cos(alpha),    np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta),    np.cos(theta)*np.cos(alpha), -1*np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [            0,                  np.sin(alpha),                  np.cos(alpha),               d],
        [            0,                              0,                              0,               1]
    ])


DHRobot_2dof = rtb.DHRobot(
    [
        rtb.RevoluteDH(
            d = 0.15, # distance up the Z axis
            alpha = 0, # X axis - pitch of effector 
            a = 0.2, # distance along the Y axis
            offset = math.radians(45) # The inital rotation of the link from the base
        ),
        rtb.RevoluteDH(
            d = 0.15, # distance up the Z axis
            alpha = 0, # X axis - pitch of effector 
            a = 0.2, # distance along the Y axis
            offset = math.radians(0) # The inital rotation of the link from the previous link
        )
    ],
    name = "Manipulator"
)

print(DHRobot_2dof)
print("Transformation Matrix:")
DHRobot_2dof.fkine(DHRobot_2dof.offset).print()

print("Translation sub vector:")
print(DHRobot_2dof.fkine(DHRobot_2dof.offset).t) # Translation sub vector
# Returns the following:
# [2.4492936e-17 4.0000000e-01 3.0000000e-01]
# x, y, and z - looks perfect on the plot.

print("Rotation sub matrix:")
print(DHRobot_2dof.fkine(DHRobot_2dof.offset).R) # Rotation sub matrix
# Not sure why this doesn't match the Transformation Matrix above?



DHRobot_2dof.plot(DHRobot_2dof.offset, limits=[-0.5, 0.5, -0.5, 0.5, 0.0, 0.5], block=True)

robot_6dof = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)   ),
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)    ),
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)    ),
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)    ),
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)    ),
        rtb.RevoluteDH(d=100,   alpha=0,    a=50, offset=math.radians(60)    )
    ],
    name="Six-Link Robot"
)
# print(robot_6dof)
# print(robot_6dof.fkine(robot_6dof.offset))
# robot_6dof.plot(robot_6dof.offset, limits=[-300.0, 300.0, -300.0, 300.0, 0.0, 600], block=True)

