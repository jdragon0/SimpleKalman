import numpy as np
import SimpleKalman as kf
import matplotlib.pyplot as plt

dt = 0.1
A = np.array([[1,dt],[0,1]])
H = np.array([1,0])[np.newaxis]
Q = np.array([[1,0],[0,3]])
R = 10

x = np.array([0,20])[np.newaxis].transpose()
P = np.identity(2)*5

pos, vel,real_vel = kf.simpleKalman(A,H,Q,R,P,x)

plt.figure(1)
plt.title("Velocity")
plt.xlabel("Time[sec]")
plt.ylabel("Velocity[m/s]")
plt.grid()
plt.plot(real_vel)
plt.plot(vel)
plt.legend(["Real velocity","Kalman Filter"])

plt.figure(2)
plt.title("Position")
plt.xlabel("Time[sec]")
plt.ylabel("Position[m]")
plt.grid()
plt.plot(pos)

plt.show()

