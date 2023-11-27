from vpython import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


g = 9.8  # 重力加速度 9.8 m/s^2
size = 0.05  # 球半徑 0.05 m
L = 0.5  # 彈簧原長 0.5m
k = 10  # 彈簧力常數 10 N/m
m = 0.1  # 球質量 0.1 kg
Fg = m * vector(0, -g, 0)  # 球所受重力向量



#---------場地------------
L = 2
scene = canvas(width=800,height=500, center=vector(0,-L*0.8,0), range=1.2*L)
floor = box(length=4,height=0.02, width=1.6, opacity=0.2)#畫地板
floor.pos = vector(0, -L*1.5, 0)
wall = box(length=0.02, height=2, width=1, color=color.white, opacity=1)#畫牆
wall.pos = vector(-2,-L*1.1,0)

#----------第一組------------
#方塊m1物件
object = box(length=0.6, height=0.6, width=0.6, color=color.white, opacity=1) #畫物體
object.pos = vector(-0.4,-1.35*L,0)#(左右,上下,前後)
#彈簧k1物件
spring = helix(radius=0.08, thickness=0.04)#畫彈簧
spring.pos= vector(-2,-1.28*L,0)#彈簧頭端的位置
spring.color = vector(0.7,0.5, 0.2)
spring.axis = 1.6 * vector(1,0,0)
#阻尼器B1(外殼)
damperB = cylinder(radius=0.08, thickness=0.04)
damperB.pos = vector(-2, -1.45*L, 0)
damperB.color=vector(0.4,0.1,0.2)
damperB.axis = 0.6 * vector(1, 0, 0)
#阻尼器b1
damperb = cylinder(radius=0.04, thickness=0.04)
damperb.pos =vector(-1.4, -1.45*L, 0)
damperb.color = vector(0.3, 0.5, 0.1)
damperb.axis = 1*vector(1, 0, 0)

#----------第二組---------------
#彈簧k2物件
spring2 = helix(radius=0.08, thickness=0.04)# 畫彈簧
spring2.pos = vector(-0.1,-1.28*L,0)#彈簧頭端的位置
spring2.color = vector(0.7,0.5,0.2)
spring2.axis = 1.6 * vector(1,0,0)
#方塊m2物件
object2 = box(length=0.6, height=0.6, width=0.6, color=color.white, opacity=1)#物體
object2.pos = vector(1.5, -1.35*L, 0)
#阻尼器c2
damperc = cylinder(radius=0.04, thickness=0.04)
damperc.pos = vector(0.5, -1.45*L, 0)
damperc.color=vector(0.3,0.3,0.6)
damperc.axis = 1 * vector(1, 0, 0)
#阻尼器C2(外殼)
damperC = cylinder(radius=0.08, thickness=0.04)
damperC.pos = vector(-0.1, -1.45*L, 0)
damperC.color = vector(0.6,0.5, 0.2)
damperC.axis = 0.6* vector(1, 0, 0)

#系統參數
m1 = 1
m2 = 1
b1 = 1
b2 = 1
k1 = 1
k2 = 1
#轉移函數係數
A4 = m1*m2
A3 = b2*m1+b1*m2+b2*m2
A2= k2*m1+b1*b2+k1*m2+k2*m2
A1 = k2*b1+b2*k1
A0 = k1 * k2
#X2
B1 = b2
B0 = k2
#X1
C2 = m1
C1 = b1+b2
C0 = k1+k2

t = 0.0001
dt = 0.002
inputAmplitude = 1.0
period = 2 * 10
f = 1 / period
w = 2 * np.pi * f
N = 3
sample = 50
t = np.linspace(0, period*N, num=period*N*sample,endpoint=False)

num1 = [B1,B0]
den1 = [A0,A1,A2,A3,A4]
system1 = signal.TransferFunction(num1, den1)
input_square = signal.square(w * t)
t_square,y_square1,x_square = signal.lsim(system1,input_square,T=t)


num2 = [B1,B0]
den2 = [C2,C1,C0]
system2 = signal.TransferFunction(num2, den2)
t_square,y_square2,x_square = signal.lsim(system2,input_square,T=t)

for i in range(t.size):
    rate(100)
    #---------spring 和 damper 的連動------------
    object2.pos = vector(1.2+0.5*y_square1[i], -1.35*L,0)
    object.pos = vector(-0.4+0.5*y_square2[i], -1.35*L,0)

    damperC.pos.x = object.pos.x 
    damperc.pos.x = object.pos.x 
    
    damperb.axis = vector((1.4+object.pos.x),0,0)
    damperc.axis = vector((object2.pos.x - object.pos.x),0,0)
    
    spring2.pos.x = object.pos.x
    spring2.axis = vector(object2.pos.x - object.pos.x,0,0)
    spring.axis = vector(object.pos.x - wall.pos.x,0,0)