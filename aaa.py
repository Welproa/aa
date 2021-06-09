import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x=np.linspace(-1,1,100)
y=1/(1+25*x**2)
plt.ylim(-1,1.1)
plt.plot(x,y,linewidth=1.0,color='black',label='f(x)',linestyle='-')


def f(x,n):
    x1=np.linspace(-1,1,n+1,endpoint=True)#等距生成n+1个数
    fq=0
    for xk in x1:
        fz=1
        fm=1
        for xi in x1:
            #𝑞𝑘(𝑥) 的分子分母
            if xk!=xi:
                fz=fz*(x-xi)
                fm=fm*(xk-xi)
        qqq=(fz/fm)*(1/(1+25*xk**2))
        fq+=qqq#级数求和
    return fq

y1=[f(xi,4) for xi in x]
y2=[f(xi,8) for xi in x]
y3=[f(xi,12) for xi in x]

plt.plot(x,y1,linewidth=1.0,color='red',label='n=5',linestyle='--')
plt.plot(x,y2,linewidth=1.0,color='blue',label='n=9',linestyle=':')
plt.plot(x,y3,linewidth=1.0,color='green',label='n=13',linestyle='-.')
plt.legend(loc='lower center')
plt.title('203772998 李佳康')
plt.show()
