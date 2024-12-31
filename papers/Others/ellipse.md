
### 正弦波变换成椭圆了吗？
![fig1](ellipse1.png)
(a) 子图中先出现的正弦波在 $x$ 时刻与 $lag=T$ 时的采样分别记为：
$$
m=\sin(ax+b),\;n=\sin(ax+b +T)
$$
不妨令：$ax+b=f$ 则有，
$$
m=\sin{f},\;n=\sin(f+T)\\
$$
展开可得到：
$$
\sin(f+T)=\sin{f}\cos{T}+\cos{f}\sin{T}=m\cos{T}+\cos{f}\sin{T}=n \\
\;\\
\cos f = \frac{n-m\cos T}{\sin T}
$$
注意到 $\sin^2f+\cos^2f=1$，
$$
m^2+(\frac{n-m\cos T}{\sin T})^2=1
$$
化简得到
$$
m^2+n^2-2\cos T mn-\sin^2 T=0
$$
由此可以得到 $m,n$ 满足椭圆一般方程 
$$
Ax^2+By^2+Cxy+Dx+Ey+F=0
$$
### 什么时候是个圆？
当选取的 lag 与正弦波的 $a$ 满足如下条件时，
$$
T=\frac{\pi}{2a}+\frac{k\pi}{a}
$$
即$-2\cos T=0$ 时，$m,n$ 在一个圆上。