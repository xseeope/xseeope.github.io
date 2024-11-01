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
u{OOS}=E[U(R^{\pi_t}_t)],\;t>T
$$
当 $N/T \neq 0$ 的情况出现时，作者认为这时候 *complexity* 就出现了，并会导致用像上面一样用矩来估计会不准确，产生 divergence。