import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

m1, b1, k1 = 1,1,1
m2, b2, k2 = 1,1,1

my_list=[0.01,0.1,1,10,100]
label="k1/k2="

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

period = 2 * 10
f = 1 / period
w = 2 * np.pi * f
N = 3
sample = 50
t = np.linspace(0, period*N, num=period*N*sample,endpoint=False)
input_square = signal.square(w * t)

y_step=[]

y_square=[]

for sys in system:
    '''Step response'''
    t_step, y_step1 = signal.step(sys, T = t, N = period*N*sample)
    y_step.append(y_step1)
    '''Square response'''
    t_square,y_square1,x_square = signal.lsim(sys,input_square,T=t)
    y_square.append(y_square1)

'Plot figure'
#<step>
plt.subplot(211)
plt.title("4rd system step response")
input_step=[1] * t.size
plt.plot(t_step,input_step , color='gray', label="Input: Step")
for i in range(len(my_list)):
    plt.plot(t_step, y_step[i], label=label+str(my_list[i]))
plt.xlabel('time(sec)')
plt.ylabel( 'Amplitude')
plt.grid()
plt.legend()
#<square>
plt.subplot(212)
plt.title("4rd system square response")
plt.plot(t_square, input_square, color='gray', label="Input: Square")
for i in range(len(my_list)):
    plt.plot(t_square, y_square[i], label=label+str(my_list[i]))
plt.xlabel('time(sec)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()
# save_path = 'C:/Users/ASUS/薇如/文件/大學/System Dynamics/final project/b1除b2/Figure_'+'b1除b2'+'_'+str(i)+'.png'
# fig = plt.gcf()
# fig.set_size_inches(18,12)
# plt.savefig(save_path)
# plt.clf()
