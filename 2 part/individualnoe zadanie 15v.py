Z №1

print('zadanie №1')
import numpy as np
myA=np.array([[1.7,1.8],[1.19,1.72]])
myB=np.array([0.75,0.43])
print(myA[0,],"*X1=",myB[0])
print(myA[1,],"*X2=",myB[1])
slv = np.linalg.solve(myA, myB)
print("Reshenie=", slv)

Z №2

print('zadanie №2')
import numpy as np
myA=np.array([[1.38,1.51,1.96],[1.18,1.02,1.44],[1.76,1.05,1.57]])
myB=np.array([0.26,0.94,0.18])
print(myA[0,],"*X1=",myB[0])
print(myA[1,],"*X2=",myB[1])
print(myA[2,],"*X3=",myB[2])
slv = np.linalg.solve(myA, myB)
print("Reshenie=", slv)

Z №3

print('zadanie №3')
import numpy as np 
myA=np.array([[1.63,1.82],[1.91,1.24]])
myB=np.array([0.03,0.06])
print(myA[0,],"*X1=",myB[0])
print(myA[1,],"*X2=",myB[1])
slv = np.linalg.solve(myA, myB)
print("Reshenie=", slv)

Z №4

print('zadanie №4')
import numpy as np
myA=np.array([[1.92,1.03,1.90,1.62],[1.95,1.06,1.06,1.70],[1.84,1.78,1.37,1.33],[1.90,1.67,1.95,1.40]])
myB=np.array([0.03,0.51,0.01,0.82])
print(myA[0,],"*X1=",myB[0])
print(myA[1,],"*X2=",myB[1])
print(myA[2,],"*X3=",myB[2])
print(myA[3,],"*X4=",myB[3])
slv = np.linalg.solve(myA, myB)
print("Reshenie=", slv)

Z №5

print('zadanie №5')
import numpy as np
myA=np.array([[1.35,1.96,1.28,1.16,1.9],[1.3,1.8,1.73,1.87,1.33],[1.08,1.74,1.24,1.02,1.24],[1.34,1.29,1.42,1.39,1.92],[1.21,1.70,1.76,1.35,1.32]])
myB=np.array([0.84,0.62,0.74,0.80,0.44])
print(myA[0,],"*X1=",myB[0])
print(myA[1,],"*X2=",myB[1])
print(myA[2,],"*X3=",myB[2])
print(myA[3,],"*X4=",myB[3])
print(myA[3,],"*X5=",myB[4])
slv = np.linalg.solve(myA, myB)
print("Reshenie=", slv)
