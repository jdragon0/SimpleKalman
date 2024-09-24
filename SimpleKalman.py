import numpy as np

def getPos(dt,prev_pos,vel):
    w = np.random.normal()*10
    v = np.random.normal()*10

    npos = prev_pos + (vel+w)*dt + v
    realPos = npos-v
    realVel = vel+w
    return npos , realPos, realVel

def simpleKalman(A,H,Q,R,P,x):
    pos = []
    vel = []
    realVel=[]
    dt = 0.1
    realPos = 0
    for i in range(100):
        xp = A@x
        Pp = A@P@A.transpose()+Q

        z,p,v = getPos(dt,realPos,80)
        realPos = p
        K = Pp@H.transpose()*np.linalg.inv(H@Pp@H.transpose()+R)
        x = xp+K@(z-H@xp)
        P = Pp - K@H@Pp

        pos.append(x[0])
        vel.append(x[1])
        realVel.append(v)
    return pos , vel, realVel
