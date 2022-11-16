#Finding Initial/BaseFrame Rotation of the Rotation Matrix 

import numpy as np
Theta1 = 0                          #Initial angle 
Theta2 = 0                          #initial angle
Theta1 = (Theta1/180)*np.pi         #
Theta2 = (Theta2/180)*np.pi

R0_1 = [[np.cos(Theta1), -np.sin(Theta1),0],[np.sin(Theta1) ,np.cos(Theta1),0 ],[0,0,1]]
R1_2 = [[np.cos(Theta2), -np.sin(Theta2),0],[np.sin(Theta2) ,np.cos(Theta2),0 ],[0,0,1]]


R0_2 = np.dot(R0_1,R1_2)
print(R0_2)


#Finding Roataion when Theta2 is set to 90 degree
print("\n")
Theta1 = 0                          #Initial angle 
Theta2 = 0                          #initial angle
Theta1 = (Theta1/180)*np.pi         #
Theta2 = (Theta2/180)*np.pi

R0_1 = [[np.cos(Theta1), -np.sin(Theta1),0],[np.sin(Theta1) ,np.cos(Theta1),0 ],[0,0,1]]
R1_2 = [[np.cos(Theta2), -np.sin(Theta2),0],[np.sin(Theta2) ,np.cos(Theta2),0 ],[0,0,1]]


R0_2 = np.dot(R0_1,R1_2)
print(R0_2)