import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#---系統參數-----
m1, b1, k1 = 1,1,1
m2, b2, k2 = 1,1,1

#---預計要模擬的參數-----
my_list=[0.01,0.1,1,10,100]
label="k1/k2="

#---製作不同參數的轉移函數---
system=[]
for i in my_list:
    #---轉移函數係數----
    k1=1
    k2=k1/i
    A0=m1*m2
    A1=b2*m1+b1*m2+b2*m2
    A2=k2*m1+b1*b2+k1*m2+k2*m2
    A3=k2*b1+b2*k1
    A4=k1*k2

    B0=k2
    B1=b2
    
    #---轉移函數設定----
    num = [B1,B0]
    den = [A0,A1,A2,A3,A4]
    system1 = signal.TransferFunction(num, den)
    system.append(system1)

#---x軸設定-----    
f = np.logspace(-2, 3, num=1000)  
w = 2 * np.pi * f

#---y軸響應(大小、相位)-----
mag=[]
phase=[]
for sys in system:
    w, mag1, phase1 = signal.bode(sys, w)
    mag.append(mag1)
    phase.append(phase1)

#---大小/頻率-----
plt.subplot(211)
for i in range(len(my_list)):
    plt.semilogx(w, mag[i], label=label+str(my_list[i]))
plt.title("4th system Bode diagram")
plt.xlabel('frequency(rad/sec)')
plt.ylabel('magnitude(db)')
plt.legend()
plt.grid()

#---相位/頻率-----
plt.subplot(212)
for i in range(len(my_list)):
    plt.semilogx(w, phase[i], label=label+str(my_list[i]))
plt.xlabel('frequency(rad/sec)')
plt.ylabel('phase(degree)')
plt.legend()
plt.grid()
fig = plt.gcf()   
fig.set_size_inches(18,12)
plt.show()