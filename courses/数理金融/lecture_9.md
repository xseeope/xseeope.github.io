# Dynamic optimization

## Discrete-time dynamic programming




## Continuous-time deterministic dynamic programming

Give $x_0 \in \Re$, consider the following control system:

$$
\begin{cases}
 \dot x(t)= \dfrac{\mathrm{d}x}{\mathrm{d}t} = b(t,\ x(t),\ u(t)),& t \in [0,\ T] \\
 x(0) = x_0
\end{cases}
\tag{1}
$$

$t$: 可以理解为被积分的变量，一般代表时间

$x(t)$: 可以理解为起点

$u(t)$: 控制集，可以理解为控制起点到终点经过的路径

>where the control $u(\cdot): [0,\ T] \to U$ belongs to the admissible control set, given by $\mathcal{A}[0,\ T]=\{u(\cdot) \text{ is measurable in } [0,\ T]\}$, with $U$ being a metric space, $T>0$, and $b: [0,\ T]\times \Re \times U \to \Re$ a given map

The optimal control problem is to maximize the value functional:

$$
J(u(\cdot)) =  \int_0^{T} f(t,\ x(t),\ u(t))~\mathrm{d}t + h(x(T)), \quad over \mathcal{A}[0,\ T] \tag{2}
$$

for some given payoff maps $f$ and $h$.

起点从 0 变为 $s$：

(1) 式变为：

$$
\begin{cases}
 \dot x(t)= \dfrac{\mathrm{d}x}{\mathrm{d}t} = b(t,\ x(t),\ u(t)),& t \in [\textcolor{red}{s},\ T] \\
 \textcolor{red}{x(s) = y}
\end{cases}
$$

(2) 式变为：

$$
J(s,y;u(\cdot)) =  \int_{\textcolor{red}{s}}^{T} f(t,\ x(t),\ u(t))~\mathrm{d}t + h(x(T))
$$

Now we define the following function (value function):

$$
\begin{cases}
V(s,y)=\operatorname*{sup}_{u(\cdot)\in\mathcal{A}[s,T]} J(s,y;u(\cdot)),\; \text{for any}(s,y)\in[0,T)\times \Re \\
V(T,y)=h(y)
\end{cases}
$$

$h(y)$ 代表在 $t=T$ 时的价值

