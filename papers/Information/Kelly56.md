# A New Interpretation of Information Rate
- J. L. Kelly, JR.

## Abstract

考虑这样一个通信信道，该信道的输入符号被表示为一个随机事件的结果，如果该随机事件是一个公平的赌博（即赔率和真实概率一致），则一个赌徒可以使用这个信道达成他财富的指数增长，其财富指数增长的指数比例与该信道的信息传输比率相等。且该结果可以被 generalized 到任意的赔率中。

## Introduction

香农通过概率定义一个充满噪声的信道中的传输速率。同时香农定理表明通过合适的编码，二进制数字可以在任意的一个错误率容忍度的情况下完成信道间的传输。

## The Gambler with a Private Wire

先从这样一个设想开始，假设有一个赌徒，他能通过一个特殊的信道提前知道赌博的结果之后再已原始的赔率下注，假设赔率为 1 比 1，则在 $N$ 次如此的操作之后，其财富将从初始的 $V_0$ 增长为 $2^N V_0$。定义如下的指数增长率 $G$：
$$
G=\lim _{N \rightarrow \infty} \frac{1}{N} \log \frac{V_N}{V_0}
$$

>[!TIP]
如下计算平均指数增长率：
$$
\text{log return}=\log \frac{V_N}{V_0}-1 \\
\lim N \rightarrow \infty \\
G=\frac{1}{N}(\log \frac{V_N}{V_0}-1)=\frac{1}{N}\log \frac{V_N}{V_0}
$$

现在在上面例子的基础上增加一个设想，假设信道中传输的信号错误的概率为 $p$，正确的概率为 $q$。如果其仍然遵循他先前的下注策略，即每次都压上全部身家，则其财富的期望 $\langle V_N \rangle$ 为：
$$
\langle V_N \rangle = (2q)^NV_0
$$
很明显这是一个不太聪明的策略，尾部风险过高，当 $N \rightarrow \infty$ 时，其破产概率也将收敛到 1。因此作为一个没那么笨的人，应该每次只投资一部分财产 $\mathscr{l}$，由此我们有：
$$
V_N=(1+\mathscr{l})^W(1-\mathscr{l})^LV_0 
$$
其中 $W$ 和 $L$ 分别为在总共 $N$ 次的下注中获胜和失败的概率，由此我们有：
$$
G = \lim_{N\rightarrow \infty}[\frac{W}{N}\log(1+\mathscr{l})+\frac{L}{N}\log(1-\mathscr{l})]
$$
$$
G = q\log (1+\mathscr{l})+p\log(1-\mathscr{l})
$$
求解出 $1+\mathscr{l}=2q$，$1-\mathscr{l}=2p$ 时，$G$ 有最大值：
$$
G_{max} = 1+q\log q+p\log p=R
$$
等于香农的信息传输速率。
> [!NOTE]
> 如此求解背后的假设为下注者并不是在追求收益期望的最大值（即每次都 all in），而是在追求最大化 $G$，也就是平均的指数增长率。

## The General Case

### Notation
- $p(s)$ the probability that the transmitted symbol is the $s$'th one.
- $p(r/s)$ the conditional probability that the received symbol is the $r$'th on the hypothesis that the transmitted symbol is the $s$'th one.
- $p(s,r)$ the joint probability of the $s$'th transmitted and the $r$'th received symbol.
- $q(r)$ received symbol probability
- $q(s/r)$ conditional probability of transmitted symbol on hypothesis of received symbol.
- $\alpha_s$ the odds paid on the occurrence of the $s$'th transmitted symbol, i.e., $\alpha_s$ is the number of dollars returned for a one-dollar bet (including that one dollar).
- $a(s/r)$ the fraction of the gambler's captial that he decides to bet on the occurrence of the $s$'th transmitted symbol *after* observing the $r$'th *received* symbol.

### Case of "fair" odds
只考虑独立的被传输信号和噪声。

首先考虑“公平”的赔率，即：
$$
\alpha_s = \frac{1}{p(s)}
$$
同时设想没有赌场抽水（track take），则有
$$
\sum \frac{1}{\alpha_s}=1
$$
不失一般性，假设
$$
\sum_s a(s/r)=1
$$
也就是说不论收到什么信号，赌博者都会投入全部的财富，因为他可以通过取消下注来拿回资金。我们现在有，
$$
V_N=\prod_{r,s}[a(s/r)\alpha_s]^{W_{sr}}V_0
$$
其中 $W_{sr}$ 表示接受信号 $r$ 后下注信号 $s$ 且获胜的次数。
$$
\log \frac{V_N}{V_0}=\sum_{rs}W_{sr}\log \alpha_s a(s/r)
$$
并可以得到指数增长率：
$$
G=\lim_{N\rightarrow\infty}\frac{1}{N}\log\frac{V_N}{V_0}=\sum_{rs}p(s,r)\log\alpha_sa(s/r)
$$
注意到,
$$
\alpha_s=\frac{1}{p(s)}
$$
则有，
$$
G=\sum_{rs}p(s,r)\log\frac{a(s/r)}{p(s)}\\
G=\sum_{rs}p(s,r)\log a(s/r)+H(X)
$$
其中 $H(X)$ 为香农定义的 source rate。上式 $G$ 的第一项可以求解出最大值点：
$$
a(s/r) = \frac{p(s,r)}{\sum_k p(k,r)} = \frac{p(s,r)}{q(r)}=q(s/r)
$$
则我们可以得到 $G_{max}=H(X)-H(X/Y)$，即为香农定义的 rate of transmission。