# A Mathematical Theory of Communication
- C.E. SHANNON
- The Bell System Technical Journal

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

> [!Note] Generally, a discrete channel means a system whereby a sequence of choices from a finite set of elementary symbols $S_1, \dots,S_n$ can be transmitted from one point to another.

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

>[!TIP]此处假设了 $N(t)$ 与 $t$ 的关系是近似指数的，即 $N(t) \approx AX^t$，在线性递推关系中，尤其是具有固定形式的递推关系时，指数形式的解是自然的猜测。令 $N_i(L)$ 为以转移至状态 $i$ 为结尾且长度为 $L$ 的符号块（blocks of symbols）的所有可能的数量。则我们有如下递推关系，将解的指数形式带入递推关系有
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

**Proof of Theorem 1** The Growth of the Number of Block of Symbols with a Finite State Condition

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
- $\mathbf{M}$ 为 $m\times m$ 的矩阵，$m$ 为状态的数量，其每一个元素为 $M_{ij}=\sum_SW^{-b^{(s)}_{ij}}-\delta_{ij}.$
- $\mathbf{A}$ 为 $m\times 1$ 的向量，其每一个元素为 $A_j.$
  
注意到该矩阵方程有非平凡（non-trivial）解的条件为 $det(\mathbf{M})=0$ ,也就是说 $\mathbf{M}$ 必须是奇异矩阵，若 $\mathbf{M}$ 为非奇异，只会存在平凡解 $\mathbf{A}=\mathbf{0}.$

由此条件，我们可以确定 $W$，也就是方程 $det(\mathbf{M})=0$ 的最大实数根。

回到 capacity，可以得到
$$
C=\lim_{L\rightarrow\infty}\frac{\log \sum A_jW^L}{L}=
\lim_{L\rightarrow\infty}(\frac{\log W^L}{L}+\frac{\log \sum A_j}{L})
=\log W,
$$