# A one-period binomial model

## 期权定价

初始时刻是 $t=0$, 终止时刻是 $t=1$

概率空间 $\left(\Omega,\mathcal{F},\mathbb{P}\right)$ 刻画了不确定性:

* $\Omega = \{H,T\}$

* $\mathcal{F} = 2^{\Omega}$

* $\mathbb{P}\{H\} = p_1 \in (0,1) \qquad \mathbb{P}\{T\} = p_2 = 1 -p_1$

市场上有三种资产，两个是基础资产，第三个是衍生资产：

* 无风险资产，也即政府债券，收益率 $r > 0$，定价过程表示为 $B: B_1 = B_0(1+r)$

* 股票，初始价格为已知常数 $S_0$，定价过程表示为 $S: S_1 = (s_1,s_2)' = (uS_0,dS_0)'$

* 看涨期权，执行价格为 K，终止时刻价值为：$V_1 = (S_1-K)^{+}$

**目标：求解期权在 $t=0$ 时的价格 $V_0$**

>[!TIP|label:提示]
>为衍生资产定价，可以通过将基础资产组合起来，使得组合的现金流与衍生资产的现金流相同，从而组合的价值就是衍生资产的价值

方法：使用基础资产构造一个组合，使其现金流与期权的现金流相同，该组合的价值也即期权的价值

1. $t=0$ 时卖出看涨期权，得到 $V_0$

2. 买入 $\Delta_0$ 股股票来对冲风险

3. 剩下的 $V_0-\Delta_0 S_0$ 用来购买无风险资产 ($V_0-\Delta_0 S_0$ 若为负，代表卖出无风险资产)

4. $t=1$ 时需要支付 $V_1$

在一个无套利的市场，$t=1$ 时，通过卖出期权投资两种基础资产的价值应当等同于期权的价值：

$$
(V_0-\Delta_0 S_0)(1+r) + \Delta_0 S_1 = V_1
$$

考虑股票的两种状态，分别代入:

$$
\begin{aligned}
    (V_0-\Delta_0 S_0)(1+r) + \Delta_0 S_0u &= V_1(u)\\
    (V_0-\Delta_0 S_0)(1+r) + \Delta_0 S_0d &= V_1(d)
\end{aligned}
$$

求解 $V_0,\Delta_0$：

$$
V_0 = \dfrac{\widetilde{p}_u V_1(u) + \widetilde{p}_d V_1(d)}{1+r} \tag{1}
$$

$$
\Delta_0 = \dfrac{V_1(u)-V_1(d)}{S_1(u)-S_1(d)} \quad or \quad \dfrac{V_1(u)-V_1(d)}{S_0u-S_0d}
$$

其中

$\widetilde{p}_u = \dfrac{1+r-d}{u-d}, \qquad \widetilde{p}_d = 1 - \widetilde{p}_u$

>[!NOTE|label:提示]
>证明：$d<1+r<u \\$
>若 $1+r \leq d$，则股票的收益率恒大于无风险收益率，股票即使下跌收益率也大于无风险收益率，市场上便没有对无风险资产的需求 $\\$ 同理，若 $1+r \geq u$ 也不成立

## 风险中性定价方法

考虑概率测度 $(\widetilde{p}_u, \widetilde{p}_d)$，(1) 式可以写成：

$$
V_0 = \frac{\mathrm{E}^{\widetilde{\mathbb{P}}}(V_1)}{1+r}
$$

在风险中性世界中，投资者只要求无风险收益率，因此概率测度 $(\widetilde{p}_u, \widetilde{p}_d)$ 又称为风险中性概率测度

## 随机折现因子(stochastic discount factor)

考虑两个状态的模型，有两个阿罗证券：$(1,0)',(0,1)'$

由此可以确定状态价格 $\psi:$

$\qquad \psi_1=\widetilde{p}_1/(1+r),\quad \psi_2=\widetilde{p}_2/(1+r)$

根据 SDF 的定义：

$\qquad \pi \equiv (\pi_1,\pi_2)'= (\dfrac{\psi_1}{p_1}, \dfrac{\psi_2}{p_2})' $

$X\equiv(x_1,x_2)'$ 的价格为：

$
\qquad
\begin{aligned}
V_x&=x_1\psi_1+x_2\psi_2\\
\\
&=p_1\pi_1x_1 + p_2\pi_2x_2\\
\\
&= \mathrm{E}(X \pi)
\end{aligned}
$

>三者知道其中一个便可以得到另外两个：$\\$
>In a word, it suffices to know risk neutral probability measure, or state price vector, or stochastic discount factor in order to determine the price of a claim.