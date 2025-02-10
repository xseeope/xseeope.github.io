# 20250117祝纪元报告
对于 false alarm 的约束，使用 Lorden 在 1971 年的文章使用的 Lorden's criterion 即 worst-case average detection delay，即 WADD，和 average running length，即 ARL。令 $\mathcal{F}_t$ 为序列中前 $t$ 个样本 $\pmb{y}_1,\pmb{y}_2,\cdots,\pmb{y}_t$ 的 $\sigma$-algebra。定义停止时刻 stopping time $\tau$，其性质为对所有 $t$，都有事件 $\{\tau=t\} \in \mathcal{F}_t$。对于 WADD 与 ARL 有如下定义：
$$
\text{WADD}(\tau) \triangleq \sup_{t_0>1} \text{esssup} \mathbb{E}_{t_0} [(\tau - t_0)^+|\pmb{y}_1,\cdots,\pmb{y}_{t_0-1}],\\
\;\\
\text{ARL}(\tau) \triangleq \mathbb{E}_\infty[\tau], \tag{6}
$$
其中 $\mathbb{E}_{t_0}$ 和 $\mathbb{E}_\infty$ 分别为概率测度 $\mathbb{P}_{t_0}$ 和 $\mathbb{P}_\infty$ 下的期望。现在，我们可以说我们要设计的针对 QCD 问题的算法目标具体为在 ARL 约束的条件下最小化 WADD：
$$
\inf_{\tau:\text{ARL}(\tau)\geq \gamma} \text{WADD}(\tau), \tag{7}
$$
其中 $\gamma >0$ 为预先设定的阈值。

> [!NOTE]Q：为什么 ARL 与 WADD 的概率测度不同？A：ARL 的含义为在未发生变换的情况下，算法报警的期望长度；WADD 则是在变换发生后，算法报警的最坏的平均检测时间。

>[!TIP]式（6）对 WADD 的定义中 esssup 的含义为 essential supremum，本质上确界。其与常规的 sup 的区别在于后者只考虑测度大于 0 的自变量集合。一个孤立不连续的极大值点可以是函数的上确界，但不会是本质上确界。

## Universal Lower Bound on WADD

注意到任意 AR(q) 模型都可以表示为一个 AR(1) 模型，
$$
\pmb{x}_t=\pmb{A}\pmb{x}_{t-1}+\pmb{\omega}_t, \tag{8}
$$
其中 $\pmb{A}\in \mathbb{R}^{K\times K}$ 为系数矩阵且可逆。同时设定初始的干扰信号即 $\pmb{x}_{t_0}$ 服从概率密度函数为 $f_1(\pmb{x}_{t_0})$ 的高斯分布，且独立于变换发生前的观测值。同时假设 $\pmb{A}$ 的 operator norm 小于 1，这可以严格保证系统的 stability。

在本节中证明了，在 $\mathbb{E}_\infty [\tau] \geq \gamma$ 的约束下，AR 的模型中任意算法的 WADD 指标的通用下界。为后续作者提出的渐进最优检测算法做铺垫。

### Forward Variable

定义前向变量 forward variable 为：
$$
\alpha_t(\pmb{x}_t)=p_{t_0}(\pmb{y}_{t_0},\cdots,\pmb{y}_{t},\pmb{x}_t). \tag{10}
$$
注意到 $\alpha_t(\pmb{x}_t)$ 是依赖于 $\pmb{y}_{t_0},\cdots,\pmb{y}_{t}$ 的，但为了方便 notation，将其看作已知的参数，这样 $\alpha_t$ 就只是 $\pmb{x}_t$ 函数。且有以下关系：
$$
p_{t_0}(\pmb{y}_{t_0},\cdots,\pmb{y}_{t})=\int \alpha_t(\pmb{x}_t)d\pmb{x}_t \tag{11}
$$
且很容易验证有以下递推关系：
$$
\alpha_{t+1}(\pmb{x}_{t+1})=\int \alpha_t(\pmb{x}_t) f(\pmb{x}_{t+1}|\pmb{x}_t)g(\pmb{y}_{t+1}|\pmb{x}_{t+1}) d\pmb{x}_t
$$
<em>
**Definition 1:** A Gaussian function $f'(\cdot):\mathbb{R}^K \rightarrow \mathbb{R}$ is a function of the form 
$$
f'(\pmb{x})=a\exp \left (
    -\frac{1}{2}(\pmb{x}-\pmb{\mu})^\top \Sigma^{-1}(\pmb{x}-\pmb{\mu})
\right ), \tag{12}
$$
where $a$ is a constant，$\pmb{\mu}\in \mathbb{R}^{K}$ is a arbitrary vector and $\Sigma \in \mathbb{R}^{K\times K}$ is a positive definite matrix.

**Lemma 1:** $\alpha_t(\pmb{x}_t)$ is a Gaussion function of $\pmb{x}_t$.
</em>

使用数学归纳法进行证明，首先在初始时刻 $t_0$，根据先前的假设 $\pmb{x}_{t_0}$ 显然是高斯的，而 $\alpha_1(\pmb{x}_{t_0})= f_1(\pmb{x}_{t_0}) g(\pmb{y}_{t_0}|\pmb{x}_{t_0})$ 相当于两个高斯分布相乘，同样也会得到高斯分布。

那么现在假设对于 $\forall t>1$ 在 $t-1$ 服从下式（13）关于 $\pmb{x}_{t-1}$ 的高斯函数，如果我们通过其推导出 $t$ 时也为高斯核函数，那我们便成功利用数学归纳法完成了对 **Lemma 1** 的证明。
$$
\alpha_{t-1}(x_{t-1}) = \frac{c_{t-1}}{\sqrt{(2\pi)^K \det(\Sigma_{t-1})}}
\cdot
\\ \;\\
\exp\left(-\frac{1}{2} (x_{t-1} - \mu_{t-1})^\top \Sigma_{t-1}^{-1} (x_{t-1} - \mu_{t-1})\right), \tag{13}
$$
其中 $c_{t-1},\pmb{\Sigma}_{t-1,\pmb{\mu}_{t-1}}$ 为某些特定的值。由递推关系可以有：
$$
\alpha_t(x_t) = \int \alpha_t(x_{t-1}) f(x_t | x_{t-1}) g(y_t | x_t) dx_{t-1}
\\
\;\\= \frac{c_t}{\sqrt{(2\pi)^K \det(\Sigma_t)}}
\exp\left(-\frac{1}{2} (x_t - \mu_t)^\top \Sigma_t^{-1} (x_t - \mu_t)\right), \tag{14}
$$

其中：
$$
 \Sigma_t = (A \Sigma_{t-1} A^\top + R_\omega)(A \Sigma_{t-1} A^\top + R_\omega + I)^{-1},\\
\;\\
\mu_t = (A \Sigma_{t-1} A^\top + R_\omega + I)^{-1} A \mu_{t-1} + \\
\;\\(A \Sigma_{t-1} A^\top + R_\omega)(A \Sigma_{t-1} A^\top + R_\omega + I)^{-1} y_t, \tag{15}   
$$
同时对于 $\frac{c_t}{c_{t-1}}$，其可以看作是 $\pmb{y}_t,\pmb{\mu_{t-1},\pmb{\Sigma}_{t-1}}$ 的函数，其展开为：
$$
\frac{c_t}{c_{t-1}} =
\frac{1}{\sqrt{(2\pi)^K \det(A \Sigma_{t-1} A^\top + R_\omega)}}
\cdot \frac{1}{\sqrt{\det((A \Sigma_{t-1} A^\top + R_\omega)^{-1} + I)}}\\
\;\\
\cdot \exp (- \frac{1}{2} ((A \mu_{t-1})^\top (A \Sigma_{t-1} A^\top + R_\omega)^{-1} (A \mu_{t-1})+
y_t^\top y_t  - \\
\;\\((A \Sigma_{t-1} A^\top + R_\omega)^{-1}(A \mu_{t-1}) + y_t)^\top  \cdot ((A \Sigma_{t-1} A^\top + R_\omega)^{-1} + I)^{-1}\cdot \\
\;\\((A \Sigma_{t-1} A^\top + R_\omega)^{-1}(A \mu_{t-1}) + y_t))). \tag{16}
$$

那么我们现在可以将 $p_{t_0}(y_t | \mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-1})$ 写成如下形式：

$$
p_{t_0}(y_t | \mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-1}) =
\frac{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_t)}{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-1})}\\
\;\\
= \frac{\int \alpha_t(x_t) dx_t}{\int \alpha_{t-1}(x_{t-1}) dx_{t-1}} = \frac{c_t}{c_{t-1}}, \tag{17}
$$

>[!NOTE]对（17）最后的一个等号的推导。根据（12）高斯核函数定义 $f'(\pmb{x})=a\exp \left (-\frac{1}{2}(\pmb{x}-\pmb{\mu})^\top \Sigma^{-1}(\pmb{x}-\pmb{\mu})\right )$，对其做积分有积分结果 $\sqrt{(2\pi)^K \det(\Sigma_{t-1})}$，此时联立（13），很容易便得到（17）的最后一个等于号。

接下来我们把目光又放回到 log 似然函数 $\log p_{t_0}(\pmb{y}_{t_0},\cdots,\pmb{y}_{t})$，其可以表示为：
$$
\log p_{t_0}(\pmb{y}_{t_0},\cdots,\pmb{y}_{t})=\\
\;\\
\log \frac{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_t)}{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-1})} + \log \frac{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-1})}{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t-2})}+\\
\;\\\cdots + \log \frac{p_{t_0}(\mathbf{y}_{t_0}, \mathbf{y}_{t_0+1})}{p_{t_0}(\mathbf{y}_{t_0})} + \log p_{t_0}(\mathbf{y}_{t_0})\\
\;\\
= \sum_{i=t_0}^t \frac{c_i}{c_{i-1}}, \tag{18}
$$
其中 $\frac{c_{t_0}}{c_{t_0-1}}=\log p_{t_0}(\pmb{y}_{t_0})$。这样的话，我们现在在 $t$ 时刻可以观测到 $\pmb{y}_t$，这时候便能很高效地更新似然函数 $\log p_{t_0}(\pmb{y}_{t_0},\cdots,\pmb{y}_{t})$。

### Universal Lower Bound on WADD

<em>

**Theorem 1:** We have that
$$
\lim_{t \to \infty} \frac{1}{t} \log \frac{p_{t_0}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t_0+t-1})}{p_{\infty}(\mathbf{y}_{t_0}, \cdots, \mathbf{y}_{t_0+t-1})} = \mathcal{K}, \tag{19}
$$
almost surely under $\mathbb{P}_{t_0}$ with $\mathcal{K}>0$. Moreover, as $\gamma \rightarrow \infty$,
$$
\inf_{\tau: \text{ARL}(\tau) \geq \gamma} \text{WADD}(\tau) \geq \frac{\log \gamma}{\mathcal{K}} \left(1 + o(1)\right). \tag{20}
$$

</em>

## Asymptotically Optimal Stopping Time

### First-Order AR Model

基于 generlized likelihood ratio（GLR）的 CuSum 算法被广泛用于 QCD 问题。在 AR 模型中，GLR 统计量被定义为：
$$
W_t=\max_{1\leq k\leq t} \sum^t_{t=k}
\log \frac{p_k(\pmb{y}_i|\pmb{y}_1,\cdots,\pmb{y}_{i-1})}{p_\infty(\pmb{y}_i|\pmb{y}_1,\cdots,\pmb{y}_{i-1})}. \tag{32}
$$
GLR 统计量衡量了观测值对两个不同分布倾向程度，其值越大说明越倾向于 $k$ 点为 change point 这个事件所对应的概率分布。那么对于设定好的阈值 $c$，CuSum 算法可以表示为：
$$
\tau_c =\inf \left \{ t:W_t \geq c \right \}. \tag{33}
$$

注意到在我们 AR 模型的设定中，$\mathbb{P}_{t_0}, p_{t_0}(\pmb{y}_t|\pmb{y}_{t_0},\cdots,\pmb{y}_{t-1})$ 均依赖于 $t_0$，因此在每个时间点我们都需要遍历 $p_k(\pmb{y}_t|\pmb{y}_{t_0},\cdots,\pmb{y}_{t-1})$ 来计算 $W_t$，这将带来无法承受的复杂度。作者提出的 *computationally efficient Erdogic CuSum algorithm* 是计算高效且渐进最优的。

从 WADD 的下界 $\frac{\log \gamma}{\mathcal{K}}$ 出发，作者希望找到一个统计量，使其在变化发生前，对 $\mathcal{K}$ 有负向的漂移，在变化发生后有正向的漂移。那么作者找到了这样一个统计量，对于任意的 $t_0$ 都有如上性质的统计量，即相似比例 likelihood ratio 为：
$$
L_t = \frac{p_1(\mathbf{y}_1, \cdots, \mathbf{y}_t)}{p_{\infty}(\mathbf{y}_1, \cdots, \mathbf{y}_t)},\tag{34}
$$
其中 $L_0=1$。那么由此可以写出 Ergodic CuSum statistic 为：
$$
S_t=\max_{0\leq i\leq t}(\log L_t-\log L_i)
=\max(0,S_{t-1},\log L_t - \log L_{t-1}). \tag{37}
$$
并有 Ergodic CuSum algorithm：
$$
\tau^{*}_c = \inf\{ t:S_t \geq c \}. \tag{38}
$$
现在对于 $L_t$ 这个统计量，可以很轻松使用（16）和（18）式进行迭代更新。

## Data-Driven Setting: Online Gradient Ascent CuSum
注意到在前面提出的 Ergodic CuSum algorithm 中最关键的 $L_t$ 统计量的迭代更新依赖于（16）和（18）式子，其中显然隐含的信息为 $A,R_{\omega}$ 是已知的，但现实情况下我们很可能是对于 change point 之后的分布是没有 knowledge 的（如网络攻击）。那么在本节中，作者引入了在 2012 年与 2018 年完善的 Online Gradient Ascent 算法去估计出 $A,R_{\omega}$，并插入回上面提出的算法中。其命名就直接为 OGA-CuSum 算法。
>[!NOTE] 其实这样也不能说对 change point 之后的分布完全没有 knowledge，至少还是假设了服从 AR 模型的。