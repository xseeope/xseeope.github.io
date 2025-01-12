# A Mathematical Theory of Communication
- C.E. SHANNON
- The Bell System Technical Journal 1948

## Introduction
**Points:**

- 通信的基本问题: 在某个点完全或近似重构在另一个点选择的消息（message）。
- 【真实消息】是【可能消息】集合中的一个元素。
- 系统必须被设计为可以处理所有【可能消息】。
- 当在可能消息的集合中选择一个消息，就产生了【信息】，所有选择的可能性是相等的。
- 如果消息集合中的元素个数是 finite 的，那么这个个数或任何这个个数的单调函数都可以是信息的度量（measure of the information）。
- 使用对数度量有以下好处：
  1. 贴近实践
  2. 符合直觉
  3. 数学上的处理更加容易

### General Communication System:
![Fig1](Shannon48Fig1.png)


*Information source* 产生消息（message）。消息的实例可以有：字母序列；关于时间的函数 $f(t)$；关于时间与其他变量的函数；多个关于多个变量的函数。

*Transmitter* 将消息（message）加工为信号（signal），使得其更适于在信道（channel）中传输。

*Channel* 用来传输信号的介质，如电线、光缆、射频带。

*Recevier* 从信号中重构消息。

*Destination* 这个消息所指向（intended）的人或实体

## Part 1: Discrete Noiseless Systems
### The Discrete Noiseless Channel
离散信道的实例可以是电报。

一般来说，离散信道（discrete channel）的含义为可以点对点传输对一个由基本符号 $S_1, \dots,S_n$组成的有限集合选择序列的一个系统。其中每一个信号 $S_i$ 都对应一个持续时间 $t_i$。

注意到每一个信号的持续时间不必相同，具体取决于如何编码，如 elementary signal 可以是固定长 5 秒，每一秒都携带 1 bit 的信息，也可以是不定长度。

> *Generally, a discrete channel means a system whereby a sequence of choices from a finite set of elementary symbols $S_1, \dots,S_n$ can be transmitted from one point to another.*

现考虑如下问题：如何度量这样的离散信道传输信息的容量（capacity）。对于固定持续时长的基本信号集合，且每个信号包含 $k$ bit 的信息，则对于一个可以每秒传输 $n$ 个基本信号的信道，其容量为 $kn$ bits 每秒。

在更一般的情形下，即信号的长度可以可以不同且仅允许特定可行的选择序列在信道中传输，如下定义信道容量：

 *Definition: The capacity $C$ of a discrete channel is give by:
 $$
 C=\lim_{T\rightarrow \infty}\frac{\log N(T)}{T}
 $$
 where $N(T)$ is the number of allowed signals of duration $T$.*

假设所有 sequence 都是可行的（allowed），那么经过 $t$ 时间，所有可能出现的信号序列的个数 $N(t)$ 为：
$$
N(t)=N(t-t_1)+N(t-t_2)+\cdots +N(t-t_n)
$$
其中 $N(t=t_i)$ 的含义显然为 $t$ 时期传输的序列以信号 $S_i$ 为结尾序列的所有可能的个数。对于一个较大的 $t$ 来说，$N(t)$ 将会渐近至 $X^t_0$，其中 $X_0$ 是如下特征方程的最大实数解：
$$
X^{-t_1}+X^{-t_2}+\cdots +X^{-t_n}=1
$$
在由 capacity 的定义可得到：
$$
C=\lim_{T\rightarrow \infty}\frac{\log N(T)}{T}=\log X_0.
$$

>[!TIP]此处假设了 $N(t)$ 与 $t$ 的关系是近似指数的，即 $N(t) \approx AX^t$，在线性递推关系中，尤其是具有固定形式的递推关系时，指数形式的解是自然的猜测。将解的指数形式带入递推关系有
$$
AX^t=AX^{t-t_1}+AX^{t-t_2}+\cdots+AX^{t-t_n}\\
\;\\
X^{-t_1}+X^{-t_2}+\cdots +X^{-t_n}=1.
$$

现设想一种稍微更复杂的情形，想象有存在一系列状态（state）$a_1, a_2, \dots,a_m$，对于每一个状态都存在对应的被允许在信道内传输的一个序列的集合。状态 $a_i$ 到状态 $a_j$ 的转移同时由状态 $a_i$ 与一个传输的特定信号所决定。

<em>**Theorem 1:** Let $b^{(s)}_{ij}$ be the duration of the $s^{th}$ symbol which is allowable in state $i$ and leads to state $j$. Then the channel capacity $C$ is allowed to $\log W$ where $W$ is the largest real root of the determinant equation:
$$
\lvert \sum_S W^{-b^{(s)}_{ij}} - \delta_{ij} \rvert = 0
$$
where $\delta_{ij}=1$ if $i=j$ and is zero otherwise.</em>

---

**Proof of Theorem 1** The Growth of the Number of Block of Symbols with a Finite State Condition

令 $N_i(L)$ 为以转移至状态 $i$ 为结尾且长度为 $L$ 的符号块（blocks of symbols）的所有可能的数量。则我们有如下递推关系，
$$
N_j(L)=\sum_{i,S}N_i(L-b^{(s)}_{ij})
$$
其中 $b^1_{ij},b^2_{ij},\dots ,b^m_{ij}$ 表示一些特别的符号（symbol）的长度，这些特别的符号在状态 $i$ 中是被允许的（allowed），并可以引导至状态 $j$。如上递推关系满足线性差分方程（linear difference equation），利用其性质可以得到当 $L\rightarrow \infty$ 时必有如下形式
$$
N_j=A_jW^L.
$$
带入有
$$
A_jW^L=\sum_{i,S}A_iW^{L-b^{(s)}_{ij}}\\
\;\\
A_j=\sum_{i,S}A_iW^{-b^{(s)}_{ij}}\\
$$
引入 Kronecker Delta：
$$
\delta_{ij}= \begin{cases}
1,\quad & i=j \\
0,\quad & i \neq j
\end{cases} 
$$
显然存在恒等式
$$
A_j=\sum_i \delta_{ij}A_i
$$
带入有
$$
\sum_i(\sum_SW^{-b^{(s)}_{ij}}-\delta_{ij})A_i=0.
$$
对于所有的状态 $j$，都满足该方程，对于这组方程可以被表示为一个矩阵方程
$$
\mathbf{M}\cdot \mathbf{A}=\mathbf{0}
$$
- $\mathbf{M}$ 为 $m\times m$ 的矩阵，$m$ 为状态的数量，其每一个元素为 $M_{ji}=\sum_SW^{-b^{(s)}_{ij}}-\delta_{ij}.$
- $\mathbf{A}$ 为 $m\times 1$ 的向量，其每一个元素为 $A_j.$
  
注意到该矩阵方程有非平凡（non-trivial）解的条件为 $det(\mathbf{M})=0$ ,也就是说 $\mathbf{M}$ 必须是奇异矩阵，若 $\mathbf{M}$ 为非奇异，只会存在平凡解 $\mathbf{A}=\mathbf{0}.$

由此条件，我们可以确定 $W$，也就是方程 $det(\mathbf{M})=0$ 的最大实数根。

回到 capacity，可以得到
$$
C=\lim_{L\rightarrow\infty}\frac{\log \sum A_jW^L}{L}=
\lim_{L\rightarrow\infty}(\frac{\log W^L}{L}+\frac{\log \sum A_j}{L})
=\log W.
$$

---

### The Discrete Source of Information

上方的讨论已经展示了，在离散情况下，一个信道中，所传输的所有可能的信号的个数的对数与时间呈线性关系。在本节中将讨论如何使用数学语言刻画信息源 information source，以及要回答这样一个问题：对于一个给定的信息源，每秒可以产生多少 bit 的信息。问题的关键在于如何有效利用信息源的统计特征，使得我们可以通过适当的编码，最大化利用信道的 capacity（reducing the required capacity of the channel）。

>[!NOTE]如在英文中字母 E 的出现频率最高，Q，X，Y，出现频率低，则可以使用较短的符号编码 E 这个消息，使用较长的符号编码 Q，X，Y。

任何可以从一个有限集合中产生符号序列的随机过程都可以被认为是一个信息源。该生成过程可以使用马尔可夫链中的状态转移矩阵描述。
> *Any stochastic process which produces a discrete sequence of symbols chosen from a finite set may be considered a discrete source.*

### The Series of Approximations to English

全部是举例，不再做笔记，可参阅原文。

### Graphical Representation of a Markoff Process

离散的信息源可以被一个马尔可夫过程描述，马尔可夫的状态转移可以用图表示。

### Ergodic and Mixed Sources

一个遍历过程（ergodic process）所产生的所有序列（sequence）都有相同的统计性质（same statistical properities）。

如果一个图（graph）存在如下性质，则其对应的过程（process）是遍历的：
1. 不存在两个孤立的部分（isolated parts），即不存在这样两个部分 A 与 B，使得任意在 A 部分的连接点（junction points）可以通过图中带方向的箭头抵达 B 部分中的任意连接点，B 部分的链接点也同样不能抵达 A 部分的连接点。
2. 图中所有回路（circuit）的长度的最大公约数为 1。回路的每条边都是同向并且是闭合的。实例：Fig 5 中的 BEBES series。

![Fig5](Shannon48Fig5.png ':size=600')

>[!NOTE]考虑这样一个序列，存在 *abc* 三种状态，$p_a(b)=1/3,\;p_a(c)=2/3,\;p_b(a)=p_c(a)=1$，则其一个典型的实例很可能是 *abacacacabacababacac*。显然该序列满足性质 1，但不满足性质 2。对于该序列如果固定采样间隔为 $2k$，则其该序列的采样的统计性质随着会随着起始点是否为 *a* 变化而变化，因此可以说该分布的不同样本存在不同的统计性质，因而也不存在统计同质性。

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

---

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

---

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

### The Entropy of an Information Source

考虑一个存在有限个状态的信息源，对于每一个可能的 state $i$，都存在一个概率集合 $p_i(j)$ 描述了在 $i$ 状态下产生（produce）符号（symbol）$j$ 出现的概率，因此对于每一个状态都存在熵 $H_i$。定义一个信息源的熵为其所有状态的熵的加权平均和，其权重为每个状态出现的概率：
$$
H=\sum_i P_iH_i=-\sum_{i,j}P_ip_i(j)\log p_i(j).
$$
显然上方定义刻画的是一个信息源每产生一个符号（symbol）的这个事件的熵，类似的我们也可以很容易得到一个平均每秒产生 $m$ 个符号的信息源每秒的熵为：
$$
H^{\prime}=mH.
$$

考虑这样一种情形，序列中的符号是独立的，则有 $H=-\sum p_i\log p_i$，其中 $p_i$ 是第 $i$ 个符号出现的概率。现考虑所有长为 $N$ 的序列中一个特殊的情况：第 $i$ 个符号在这个序列的出现次数为 $p_iN$，则该特殊的消息（message）出现的概率为：
$$
p=p^{p_1N}_1p^{p_2N}_2\cdots p^{p_nN}_n.
$$
亦可以写成
$$
\log p \approx N\sum_i p_i\log p_i\\
\;\\
\log p \approx -NH\\
\;\\
H \approx \frac{\log 1/p}{N}.
$$
<em>
**Theorem 3:** Given any $\epsilon>0, \delta>0$, we can find an $N_0$ such that the sequence of any length $N \geq N_0$ fall into two classes:
1. A set whose total probability is less than $\epsilon$.
2. The reminder, all of whose members have probabilities satisfying the inequality
   $$
   \left \lvert \frac{\log p^{-1}}{N}-H \right \rvert < \delta.
   $$
</em>

>[!NOTE] Theorem 3 说明当 $N$ 非常大的时候，我们可以通过找到最有可能出现的序列的概率来确定这个信息源的熵。

除此之外，还有其他逼近一个信息源的熵的方法。仍然考虑所有长度为 $N$ 的序列，并按照出现概率由大到小排列。定义 $n(q)$ 为：给定一个概率 $q$，我们要从上述序列中根据由大到小的概率所取序列的概率只和达到 $q$ 所需要取的个数。

<em>

**Theorem 4:**
$$
\lim_{N\rightarrow\infty}\frac{\log n(q)}{N}=H
$$
when $q$ does not equal 0 or 1.
</em>

我们可以将 $\log n(q)$ 解释为在给定概率的情况下，分辨最有可能抽到的序列的集合所需要的 bit 数。该定理另一个隐含的信息是当 $N$ 取值非常大的时候，$q$ 的取值与结论无关，都会等于 $H$。

本小节中的另外两个定理同样可以让我们直接利用消息（message）的统计特征去确定 $H$，并且是不依赖于这个信息源状态与状态转移的知识。

<em>**Theorem 5:**
Let $p(B_i)$ be the probability of a sequence $B_i$ of symbols from the source. Let
$$
G_N=-\frac{1}{N}\sum_i p(B_i)\log p(B_i)
$$
where the sum is over all sequences $B_i$ containing $N$ symbols. The $G_N$ is a monotonic decreasing function of $N$ and
$$
\lim _{N\rightarrow\infty} G_N = H.
$$
</em>

### Representation of the Encoding and Decoding Operations

在 transmitter 和 receiver 中进行 encoding 和 decoding 操作的部分都可以叫做 transducer 换能器。一个换能器可以被两个函数所描述：
$$
y_n=f(x_n, \alpha_n)\\
\;\\
\alpha_{n+1}=g(x_n,\alpha_n)
$$
where
- $x_n$ is the $n^{\text{th}}$ input symbol,
- $\alpha_n$ is the state of the transducer when the $n^{\text{th}}$ input symbol is introduced,
- $y_n$ is the output symbol (or sequence of output symbols) produced when $x_n$ is introduced if the state is $\alpha_n$,

### The Fundamental Theorem for a Noiseless Channel
<em>**Theorem 9:**
Let a source have entropy $H$, (bits per symbol) and a channel have capacity $C$ (bits per second). Then it is possible to encode the output of the source in such way as to transmit at the average rate $\frac{C}{H}-\epsilon$ symbols per second over the channel where $\epsilon$ is arbitrary small. It is not possible to transmit at an average rate greater than $\frac{C}{H}$.
</em>

即对于一个给定的固定产生信息速率为 $H$ 的信息源，和一个固定的信道容量，我们无论采取什么样的编码方式，都无法超越 $\frac{C}{H}$ 的信息传输速率。
