import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

m1, b1, k1 = 1,1,1
m2, b2, k2 = 1,1,1

my_list=[0.01,0.1,1,10,100]
label1="k1/k2="

system=[]
for i in my_list:
    # 4nd order system
    k1=1
    k2=k1/i
    A0=m1*m2
    A1=b2*m1+b1*m2+b2*m2
    A2=k2*m1+b1*b2+k1*m2+k2*m2
    A3=k2*b1+b2*k1
    A4=k1*k2

    B0=k2
    B1=b2

    num = [B1,B0]
    den = [A0,A1,A2,A3,A4]
    # system=signal.TransferFunction(num,den)
    system1 = signal.TransferFunction(num, den)
    system.append(system1)
gain=1
period = 2 * 10
f = 1 / period
w = 2 * np.pi * f
N = 3
sample = 50
t = np.linspace(0, period*N, num=period*N*sample,endpoint=False)

plt.subplot()
plt.title("4rd system square response")
input_sine = gain * np.sin(w * t)
plt.plot(t, input_sine, color='gray', label="Input: Sine")

for i in range(len(my_list)):
    t_sine,y_sine,x_sine = signal.lsim(system[i],input_sine,T=t)
    plt.plot(t_sine, y_sine, label=label1+str(my_list[i]))

plt.xlabel('time(sec)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
fig = plt.gcf()
fig.set_size_inches(18,6)
plt.show()
    # save_path = 'C:/Users/ASUS/薇如/文件/大學/System Dynamics/final project/sine/Figure_'+'b1除b2'+'_'+str(i)+'.png'

    # plt.savefig(save_path)
    # plt.clf()
