import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

m1, b1, k1 = 1,1,1
m2, b2, k2 = 1,1,1

my_list=[0.005]


for i in my_list:
    # 4nd order system
    m1=i
    m2=i
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
    system = signal.TransferFunction(num, den)

    period = 2 * 10
    f = 1 / period
    w = 2 * np.pi * f
    N = 3
    sample = 50
    t = np.linspace(0, period*N, num=period*N*sample,endpoint=False)
    '''Step response'''
    t_step, y_step = signal.step(system, T = t, N = period*N*sample)
    '''Square response'''
    input_square = signal.square(w * t)
    t_square,y_square,x_square = signal.lsim(system,input_square,T=t)

    'Plot figure'
    #<step>
    plt.subplot(211)
    plt.title("4rd system step response")
    input_step=[1] * t.size
    plt.plot(t_step,input_step , color='gray', label="Input: Step")
    plt.plot(t_step, y_step, color='blue', label="Output: Step")
    plt.xlabel('time(sec)')
    plt.ylabel( 'Amplitude')
    plt.grid()
    plt.legend()
    #<square>
    plt.subplot(212)
    plt.title("4rd system square response")
    plt.plot(t_square, input_square, color='gray', label="Input: Square")
    plt.plot(t_square, y_square,color='r', label="Output: Square")
    plt.xlabel('time(sec)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()
    # save_path = 'C:/Users/ASUS/薇如/文件/大學/System Dynamics/final project/m1m2/Figure_'+'m1m2'+'_'+str(i)+'.png'
    # fig = plt.gcf()
    # fig.set_size_inches(18,12)
    # plt.savefig(save_path)
    # plt.clf()
