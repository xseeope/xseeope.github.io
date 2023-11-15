# An optimal consumption problem

Let $r > 0$ be the risk-free rate and $R = 1 + r$. Suppose you have initial wealth level $x_0 = 10, 000$. At any time $k \in \{1,2,3\}$, your consumption and your wealth are denoted by $c_k$ and $x_k$ respectively, satisfying

$$
x_{k+1}=R(x_k-c_k);\quad k=0,1,2.
$$

You aim to maximize the following expected consumption total utility (target function):

$$
\sup\limits_{c_0,c_1,c_2\geq0}\left\{R^{-3}x_3^{0.5}+\sum\limits_{k=0}^2R^{-k}c_k^{0.5}\right\}
$$

where at any time k, your wealth level must satisfy $x_k \geq 0$. Please fix the optimal consumption $c_0, c_1, c_2$.

$\color{orange}{\mathbf{\huge{Answers:}}}$

**考虑 k=2 时：**

$$
\begin{aligned}
V_2(x_2) &=\max\limits_{c_2 \in [0,x_2]} \left\{R^{-2}c_2^{0.5}+ V_3(x_3) \right\}\\
\\
&= \max\limits_{c_2 \in [0,x_2]} \left\{R^{-2}c_2^{0.5}+R^{-3}[R(x_2-c_2)]^{0.5}  \right\} \tag{1}
\end{aligned}
$$

令

$$
\dfrac{\partial V_2(x_2)}{\partial c_2} = \frac{1}{2}R^{-2}c_2^{-0.5} + \frac{1}{2}R^{-3}[R(x_2-c_2)]^{-0.5}(-R) = 0
$$

解得：

$$
c_2 = \dfrac{Rx_2}{1+R} \tag{2}
$$

代入(1)式得：

$$
V_2(x_2) = R^{-2.5}\sqrt{(1+R)x_2}
$$

**考虑 k=1 时：**

$$
\begin{aligned}
V_1(x_1) &= \max\limits_{c_1 \in [0,x_1]} \left\{R^{-1}c_1^{0.5}+V_2(x_2)  \right\}\\
\\
&=\max\limits_{c_1 \in [0,x_1]} \left\{R^{-1}c_1^{0.5}+V_2\big(R(x_1-c_1)\big)  \right\}
\end{aligned} \tag{3}
$$

令

$$
\begin{aligned}
\dfrac{\partial V_1(x_1)}{\partial c_1} &= \frac{1}{2}R^{-1}c_1^{-0.5} + \dfrac{\partial V_2(x_2)}{\partial x_2} \dfrac{\partial x_2}{\partial c_1}\\
\\
&=\frac{1}{2}R^{-1}c_1^{-0.5} + \frac{1}{2}R^{-2.5}\sqrt{(1+R)}x_2^{-0.5} \times (-R)\\
\\
&=\frac{1}{2}R^{-1}c_1^{-0.5} + \frac{1}{2}R^{-2.5}\sqrt{(1+R)}\big(R(x_1-c_1)\big)^{-0.5} \times (-R)\\
\\
&=0
\end{aligned}
$$

解得:

$$
c_1 = \dfrac{R^2x_1}{1+R+R^2} \tag{4}
$$

代入(3)式得：

$$
V_1(x_1) = R^{-2}\sqrt{(1+R+R^2)x_1}
$$

**考虑 k=0 时：**

$$
\begin{aligned}
V_0(x_0) &= \max\limits_{c_0 \in [0,x_0]} \left\{R^0c_0^{0.5}+ V_1(x_1) \right\}\\
\\
&=\max\limits_{c_0 \in [0,x_0]} \left\{c_0^{0.5}+ V_1\big(R(x_0-c_0)\big) \right\}
\end{aligned} \tag{5}
$$

令

$$
\begin{aligned}
\dfrac{\partial V_0(x_0)}{\partial c_0} &= \frac{1}{2}c_0^{-0.5} + \dfrac{\partial V_1(x_1)}{\partial x_1} \dfrac{\partial x_1}{\partial c_0}\\
\\
&=\frac{1}{2}c_0^{-0.5} + \frac{1}{2}R^{-2}\sqrt{1+R+R^2}\ x_1^{-0.5} \times (-R)\\
\\
&=\frac{1}{2}c_0^{-0.5} + \frac{1}{2}R^{-2}\sqrt{1+R+R^2}\ \big(R(x_0-c_0)\big)^{-0.5} \times (-R)\\
\\
&=0
\end{aligned}
$$

解得:

$$
c_0 = \dfrac{R^3x_0}{1+R+R^2+R^3} \tag{6}
$$

代入(5)式得：

$$
\begin{aligned}
V_0(x_0) &= R^{-1.5}\sqrt{(1+R+R^2+R^3)x_0}\\
\\
&= 100R^{-1.5}\sqrt{1+R+R^2+R^3}
\end{aligned}
$$

<hr align = "center" width="90%" size = 5 color = 'lightgreen'/>

根据 $x_1 =R(x_0-c_0) $，将 (6) 式代入：

$$
x_1 = \dfrac{R(1+R+R^2)x_0}{1+R+R^2+R^3}
$$

代入 (4) 式：

$$
c_1 = \dfrac{R^3x_0}{1+R+R^2+R^3}
$$

根据 $x_2 =R(x_1-c_1) $，将 (4) 式代入：

$$
x_2 = \dfrac{R(1+R)x_1}{1+R+R^2}
$$

代入 (2) 式：

$$
c_2 = \dfrac{R^3x_0}{1+R+R^2+R^3}
$$

综上所述，the optimal consumption $c_0, c_1, c_2$ 满足：

$$
c_0=c_1=c_2= \dfrac{10,000R^3}{1+R+R^2+R^3}
$$