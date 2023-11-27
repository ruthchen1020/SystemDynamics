import numpy as np
import matplotlib.pylab as plt
from vpython import *
from scipy import signal
from scipy.integrate import odeint
from solve4th import solve4th


period = 1 * 10
f = 1 / period
w = 2 * np.pi * f
gain = 1


def diffunc1(y, t, m1, k1, b1, m2, k2, b2):
    # 輸出入訊號設定 
    U_input = gain * signal.square(w * t)
    # dy0
    dy0 = y[1]  
    # dy1
    dy1 = -(b1+b2)/m1*y[1] + b2/m1*y[2] - (k1+k2)/m1*y[0] + k2/m1*y[2] 
    # dy2
    dy2 = y[3]
    # dy3
    dy3 =  -b2/m2*y[3] + b2/m2*y[1] - k2/m2*y[2] + k1/m2*y[0] + U_input/m2

    return [dy0, dy1, dy2, dy3]

def diffunc2(y, t, m1, k1, b1, m2, k2, b2):
    # 輸出入訊號設定
    U_input = gain * 1 
    # dy0
    dy0 = y[1]  
    # dy1
    dy1 = -(b1+b2)/m1*y[1] + b2/m1*y[2] - (k1+k2)/m1*y[0] + k2/m1*y[2] 
    # dy2
    dy2 = y[3]
    # dy3
    dy3 =  -b2/m2*y[3] + b2/m2*y[1] - k2/m2*y[2] + k1/m2*y[0] + U_input/m2

    return [dy0, dy1, dy2, dy3]

m1, b1, k1 = 1.5,0.5,2
m2, b2, k2 = 1.5,0.5,2

args = (m1, k1, b1, m2, k2, b2)
time_length = 1000
t = np.linspace(0, time_length, num=time_length * 10)
y_initial = [0, 0, 0, 0]  
ans_square = odeint(diffunc1, y_initial, t, args)
ans_step= odeint(diffunc2, y_initial, t, args)

solve=solve4th(m1, k1, b1, m2, k2, b2)
wn,damp=solve.wn_and_damp()

gd_square = graph(title="4rd ODE with Square Input", xtitle="t", ytitle="value", scroll=True, fast=True, width=800, height=450, x=10, y=10,
                xmin=0, xmax=3*period, ymin=-2.5, ymax=2.5, align="left")
gd_step = graph(title="4rd ODE with Step Input", xtitle="t", ytitle="value", scroll=True, fast=True, width=800, height=450, x=10, y=10,
              xmin=0, xmax=3*period, ymin=-2.5, ymax=2.5, align="left")

Crv_square_out = gcurve(graph=gd_square, color=color.red, label="wn={:1.1}, damp={:1.1}".format(wn, damp))
Crv_square_in=gcurve(graph=gd_square, color=color.black, label="input")
Crv_step_out = gcurve(graph=gd_step, color=color.blue, label="wn={:1.1}, damp={:1.1}".format(wn, damp))
Crv_step_in = gcurve(graph=gd_step, color=color.black, label="input")

for i in range(0, t.size):
    rate(100)
    ''' square '''
    Crv_square_out.plot(pos=(t[i], ans_square[i][0]))
    Crv_square_in.plot(pos=(t[i], gain * signal.square(w * t[i])))
    ''' step '''
    Crv_step_out.plot(pos=(t[i], ans_step[i][0]))
    Crv_step_in.plot(pos=(t[i], gain*1))

