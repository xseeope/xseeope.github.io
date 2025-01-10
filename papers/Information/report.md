# 祝纪元 20250107 报告

### Ergodic and Mixed Sources

一个遍历过程（ergodic process）所产生的所有序列（sequence）都有相同的统计性质（same statistical properities）。

如果一个图（graph）存在如下性质，则其对应的过程（process）是遍历的：
1. 不存在两个孤立的部分（isolated parts），即不存在这样两个部分 A 与 B，使得任意在 A 部分的连接点（junction points）可以通过图中带方向的箭头抵达 B 部分中的任意连接点，B 部分的链接点也同样不能抵达 A 部分的连接点。
2. 图中所有回路（circuit）的长度的最大公约数为 1。回路的每条边都是同向并且是闭合的。实例：Fig 5 中的 BEBES series。

![Fig5](Shannon48Fig5.png ':size=600')

>[!NOTE]考虑这样一个序列，存在 *ac* 三种状态，$p_a(b)=1/3,\;p_a(c)=2/3,\;p_b(a)=p_c(a)=1$，则其一个典型的实例很可能是 *abacacacabacababacac*。显然该序列满足性质 1，但不满足性质 2。对于该序列如果固定采样间隔为 $2k$，则其该序列的采样的统计性质随着会随着起始点是否为 *a* 变化而变化，不存在统计同质性。

如果有一类信息源产生的序列不满足性质 1，但可以将其分成多个满足性质 1 的子图（subgraph），并且这些子图都满足性质 2。则定义该一类信息源为由一组纯净部分（pure components）组成的混合信息源（mixed source）。对于混合信息源 $L$ 及其组成成分 $L_1,L_2,L_3,\dots$，可以表示为
$$
L=p_1L_1+p_2L_2+p_3L_3\dots
$$
其中 $p_i$ 是 $L_i$ 的概率。

除非特意注明，本文所有讨论的信息源都为遍历信息源。对于一个遍历信息源，有如下性质。令 $P_i$ 为状态（state）$i$ 的概率，则在平稳时必有如下 equilibrium conditions：
$$
P_j = \sum_i P_ip_i(j).
$$
其展示了在 $N\rightarrow \infty$ 时，经过 $N$ 个符号（symbols）后处于状态 $j$ 的概率，即 $P_j(N)$。

### Choice, Uncertainty and Entropy

先前的工作已经将信息源表示为一个马尔可夫过程，那么要如何定义一个量，使其可以度量某个过程产生信息的速度。

假设我们有一组事件（event）的集合，其出现的概率为 $p_1,p_2,\dots p_n$，且已知。我们想要找到一个 measure，可以度量要出现这个 event 所需要涉及到的“选择”（choice）的量，或者说可以度量我们对结果（outcome）的不确定性有多大。

我们的 measure $H(p_1,p_2,\dots p_n)$ 应该具有如下性质：
1. $H$ 关于 $p_i$ 连续。
2. 如果所有的事件出现概率相等即 $p_1=1/n$，则 $H$ 应该是关于 $n$ 的单调递增函数。也就是说在这种情况下当可能出现事件的个数越多时，不确定性也越大，代表这个事件所需要的的选择越多。
3. 如果一个选择被分解为两个连续的选择，则其总的 $H$ 应等于子选择序列的加权平均和。在 Fig 6 展示的实例中，$H(\frac{1}{2},\frac{1}{3},\frac{1}{6})=H(\frac{1}{2},\frac{1}{2})+\frac{1}{2}H(\frac{2}{3},\frac{1}{3})$。

![Fig6](Shannon48Fig6.png ':size=600')

<em>**Theorem 2:** The only $H$ satisifying the three above assumption is of the form:
$$
H=-K\sum^n_{i=1}p_i\log p_i
$$
where $K$ is a positive constant.</em>

**Proof of Theorem 2:**
从所有事件都等可能发生的情形出发，$H(\frac{1}{n},\frac{1}{n},\dots ,\frac{1}{n})=A(n)$，由条件 3 我们可以得到在 $n=s^m$ 的情况下有
$$
A(s^m)=mA(s).
$$
类似地，可以有
$$
A(t^n)=nA(t).
$$
我们很容易找到一个 $m$ 满足
$$
s^m\leq t^n\leq s^{m+1}.
$$
取对数并除以 $n\log s$ 可以得到
$$
\frac{m}{n}\leq \frac{\log t}{\log s}\leq \frac{m}{n}+\frac{1}{n}\\
\;\\
\left\lvert \frac{m}{n}-\frac{\log t}{\log s} \right\rvert <\epsilon
$$
其中 $\epsilon$ 为任意小。现利用 $A(n)$ 的单调性，可以有
$$
A(s^m)\leq A(t^n)\leq A(s^{m+1})\\
\;\\
mA(s)\leq nA(t) \leq (m+1)A(s).
$$
同时除以 $nA(s)$，
$$
\frac{m}{n}\leq \frac{A(t)}{A(s)}\leq \frac{m}{n}+\frac{1}{n}\\
\;\\
\left\lvert \frac{m}{n}-\frac{A(t)}{A(s)} \right\rvert <\epsilon\\
\;\\
\left\lvert \frac{A(t)}{A(s)}-\frac{\log t}{\log s} \right\rvert <2\epsilon
$$
由于 $2\epsilon$ 同样为任意小，可以得到
$$
A(t)=K\log t.
$$
注意到需满足条件 2，因此需要 $K>0$。

现在利用性质 3 将情形扩展至 $n$ 个事件发生有不相同可能性的情况，其概率满足 $p_i=\frac{n_i}{\sum n_i}$，其中 $n_i$ 为整数。我们可以将该情况理解为总共有 $\sum n_i$ 个子可能（possibles），而这些子可能又被打包成 $n$ 个概率为 $p_i=\frac{n_i}{\sum n_i}$ 的可能，那么我们这时候注意到性质 3 可以有
$$
K\log \sum n_i = H(p_1,\dots,p_n)+K\sum p_i \log n_i\\
\;\\
H=K\left[ \sum p_i\log \sum n_i - \sum p_i\log n_i \right]\\
\;\\
H=-K\sum p_i \log \frac{n_i}{\sum n_i}\\
\;\\
H=-K\sum p_i \log p_i.
$$

当概率被表示为分子分母不一定有理数的分数的情况下，利用性质 1 的连续性，可以得到同样的表示。

由此，我们已经完成了对 Theorem 2 的证明并得到了熵（entropy），我们可以称呼 $H=-\sum p_i\log p_i$ 为概率集合 $p_1,\dots,p_n$ 的熵。当我们写 $H(x)$ 的时候，其含义一般为随机变量 $x$ 的熵，需要注意的是 $x$ 并不是函数的参数（argument），而更像是一个 label。

设想这样一种情形，对于连续出现的两个事件，不妨设第一个事件为 $x$，第二个事件为 $y$，定义 $p(i,j)$ 为事件 $x$ 出现结果 $i$ 的同时，事件 $y$ 出现结果 $i$ 的概率，现可以写出在给定特定的 $x$ 的结果 $i$ 时，事件 $y$ 出现 结果 $j$ 的条件概率为：
$$
p_i(j)=\frac{P(i,j)}{\sum_j p(i,j)}.
$$
且有联合事件的熵为：
$$
H(x,y)=-\sum_{i,j} p(i,j)\log p(i,j)
$$
现定义关于 $y$ 条件熵（conditional entropy）
$$
H_x(y) = H(x, y)-H(x)
$$
直接带入计算可以得到：
$$
H_x(y)=-\sum_{i,j}p(i,j)\log p_i(j).
$$



