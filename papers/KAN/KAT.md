# Kolmogorov-Arnold Transformer
ICLR 2025
- Xingyi Yang, NUS
- Xinchao Wang, NUS

本文主要工作为将 KAN 改进为 GRKAN，其不同的特性为边共享参数（group）和有理数激活函数（rational）。并将 GRKAN 代替 Transformer 中最后的 MLP 层。

## Introduction
刘子鸣等人提出的原始版本的 KAN 存在如下事实上的短板：

- *Base function.* KAN 中使用 B-spline 函数需要递归计算，与现代 GPU 的并行计算架构并不兼容。
- *Parameter and Computation Inefficiency.* 由于 KAN 中的每条边都被设计成可学习的。
- *Weight initialization* KAN 中初始化权重的操作与 MLP 类似，但是却对在事实上对收敛产生了负面影响，并且会导致不稳定性。

针对以上三个事实，本文提出了三个解决方案：

- *Rational activation* 使用 CUDA 实现了有理函数作为基函数的激活函数。
- *Group KAN* 将边分为多个 group，同一 group 之间共享相同的基函数和参数。
- *Variance-preserving initialization.* 使用能够保证不同 layer 之间方差一致性的初始化方法。


### Why original KAN fails to scale?

#### B-spline is not GPU friendly.
略。

#### Parameter and Computation Inefficiency.
参数量：KAN 所需的参数量 $O(G+K)$ 倍于 MLP，其中 $G$ 为 grid 的数量，$K$ 为阶数。

计算量：KAN 所需的计算量 $O(GK)$ 倍于 MLP。

#### Weights are not Properly Initialized
综合 LeCun，Bengio，Kaiming He 等人的观点，初始化模型参数的一个基本原则是保证 *variance-preserving*，也就是说，不论在前向还是后向过程中，信号的方差在不同层之间的转播应该保持不变。该基本原则目的也是为了保证激活值和参数在不同 layer 之间传递的稳定性。

原始的 KAN 并不满足该基本准则。初始的 B-spline 系数 $c_i$ 从 $\mathcal{N}(0, \sigma^2)$ 分布中采样，其中 $\sigma = 0.1$，而 base function 和 B-spline 函数的权重初始化则依据 Xavier 初始化，分别为 $w_s=1$ 和 $w_b \sim U \left [-\frac{6}{\sqrt{d_{in}+d_{out}}}, \frac{6}{\sqrt{d_{in}+d_{out}}} \right ]$，那么由此可以得到
$$
{Var}[\phi(x)]={Var}\left[w_b \operatorname{silu} (x)\right]+{Var}\left[w_s \operatorname{spline}(x)\right]=3 \mathbb{E}\left[\operatorname{silu}^2(x)\right]+\mathbb{E}\left[\operatorname{spline}^2(x)\right]
$$
>[!attention] 要推导出上式，隐含假设为 $d_{in}+d_{out}=4$.

现假设输出 $x\sim \mathcal{N}(0,\sigma_x^2)$，且 B-spline 的阶数 $k=0$，则有：
$$
\mathbb{E}[\text{spline}^2(x)]=\sum_i c^2_i Var[B_i(x)]=\sigma^2\sum_i Var[B_i(x)]=\sigma^2=0.01
$$
对于基函数也就是 SiLU，其方差可以由数值方法得到为 $\mathbb{E}(\text{silu}^2(x))\approx 0.355\sigma^2_x$. 那么结合基函数和样条函数的方差可以得到 $Var[\phi(x)]\approx 0.01+1.064\sigma_x^2 \neq Var[x]$