# Universal Portfolio Shrinkage
- Byran Kelly
- Semyon Malamud
- Mohammad Pourmohammadi
- Fabio Trojani

## Description of the problem
（一个很常规设定）考虑 $N$ 个资产（当然也可以是因子）。其超额收益是一个随机过程 $F_t \in \mathbb{R}^N$，$t>0$。在一个*有完美信息*的环境中，一个 economic agent 会去最大化如下的二次效用函数：
$$
U(R^\pi_t)=R^\pi_t-\frac{1}{2}(R^\pi_t)^2
$$
其中：
$$
R^\pi_t=\pi'F_t
$$
可以解出：
$$
\pi_*=E[FF']^{-1}E[F]
$$
> [!NOTE]
> 易见 $R^\pi_t=1=\pi'F_t$ 时效用函数取得最大值
> $$
\pi'F_t=1 \\
(\pi'F_t)'=1 \\
F'_t\pi=1\\
F_tF'_t\pi=F_t\\
\pi = (F_tF'_t)'F_t
$$

对于一个处于*真实世界*的 economic agent，假设他只能观察到过去 $T$ 时期的样本，（而且这人是个频率派），则他的估计为：
$$
\bar{E}[FF']=\frac{1}{T}\sum^T_{t=1}F_tF_t'\\
\bar{E}[F] = \frac{1}{T}\sum^T_{t=1}F_t
$$
其样本外效用为：
$$
u^{OOS}=E[U(R^{\pi_t}_t)],\;t>T
$$
当 $N/T \neq 0$ 的情况出现时，作者认为这时候 *complexity* 就出现了，并会导致用像上面一样用矩来估计会不准确，产生 divergence。

### Shrinkage of the covariance matrix

对协方差矩阵做 PCA 并生成 principal component portfolios 被认为是一种有效的降噪方法（如取 top-k 个主成分做 shrinkage）。

延续上小节的 notations，在 real world 中，我们观测到的 empirical covariance matrix 不妨记为 $\bar{E}[FF']$，并对其做特征值分解得到 $\bar{E}[FF']=Udiag(\lambda)U'$。利用其互相正交的特征向量构造出正交的主成分投资组合，不妨将第 $i$ 个主成分资产的预估的收益记作 $\bar{R}^{PC}_{i,t}=U'F_t$。

这时候，我们已经从原来 $N$ 维的资产空间（$F_t \in \mathbb{R}^N$）转移到了 $K$ 维的资产空间（$F^{PC}_t \in \mathbb{R}^K$）中，这里每一个资产都是正交的（太好了）。虽然资产空间略有不同，但是我们的 economic agent 不变，仍然遵循
$$
U(R^\pi_t)=R^\pi_t-\frac{1}{2}(R^\pi_t)^2
$$
的二次效用函数，那么我们做一样的计算可以得到最优权重为：
$$
\bar{\pi}_*=E[F^{PC}{F^{PC}}']^{-1}E[F^{PC}]
$$
注意到 $E[F^{PC}{F^{PC}}']$ 是一个对角阵，那么我们很容易将我们的 $\bar{\pi}_*$ 带入到我们的策略中得到组合收益为：
$$
R^{\bar{\pi}}_t=\bar{\pi}_*\cdot F^{PC}\\
\:\\
R^{\bar{\pi}}_t = \sum_{i=1}^{N} \frac{\overline{R}_i^{PC}}{\lambda_i} R_{i,t}^{PC}
$$
>[!tip]
>$E[F^{PC}{F^{PC}}']^{-1}=diag(\frac{1}{\lambda})$

显然，有效组合的权重将完全被对每个 PC 组合的 risk-return tradeoff（$ \frac{\overline{R}_i^{PC}}{\lambda_i} $）的估计确定。