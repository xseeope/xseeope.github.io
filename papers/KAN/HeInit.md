 # Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification
ICCV 2015, Microsoft Research
- Kaiming He
- Xiangyu Zhang
- Shaoqing Ren
- Jian Sun


## Introduction
标题中的Rectifiers 主要指的是 ReLU 等激活函数及其变体。本工作主要包含两部分：提出 Parametric ReLU，以及一个新的初始化方法。

## Parametric ReLU
PReLU：
$$
f\left(y_i\right)= \begin{cases}y_i, & \text { if } y_i>0 \\ a_i y_i, & \text { if } y_i \leq 0\end{cases}
$$
其中 $a_i$ 是可学习的参数，如果 $a_i=0$，则其实际上为传统的 ReLU，如果 $a_i$ 是一个固定的且值比较小的数，则其实际上为 LeakyReLU。

## Initialization of Filter Weights for Rectifiers
本部分提出的初始化方法的中心思想在于 layer 输出的方差应保持不变。
> A proper initialization method should avoid or magnifying the magnitudes of input signals exponentially.

对于一个卷积层，其在激活前的响应为：
$$
\mathbf{y}_l = W_l\mathbf{x}_l+\mathbf{b}_l.
$$
其中 $l$ 为 layer 的 index。$\mathbf{x}_l=f(\mathbf{y}_l)$，$f$ 为激活函数。假设 $\mathbf{x}_l$ 中的元素是互相独立的（mutually independent），则有：
$$
Var[y_l]=n_lVar[w_lx_l],
$$
其中 $n_l$ 为连接的个数。如令 $w_l$ 的均值为 0 则可以有：
$$
Var[y_l]=n_lVar[w_l]E[x_l]^2
$$
注意到由于使用的是 ReLU 激活函数，所以可以有 $E[x_l]^2=\frac{1}{2}Var[y_{l-1}]$，由此我们可以得到：
$$
Var[y_l]=\frac{1}{2}n_lVar[w_l]Var[y_{l-1}].
$$
先将两层之间的关系递推到所有层则有：
$$
\operatorname{Var}\left[y_L\right]=\operatorname{Var}\left[y_1\right]\left(\prod_{l=2}^L \frac{1}{2} n_l \operatorname{Var}\left[w_l\right]\right) .
$$
那么为满足方差不变需要有：
$$
\frac{1}{2} n_l \operatorname{Var}\left[w_l\right]=1,\;\; \forall l.
$$
那么现在可以得到初始化方法 $w\sim \mathcal{N}(0, \sqrt{2/n_l})$，且网络 bias 为 0。
