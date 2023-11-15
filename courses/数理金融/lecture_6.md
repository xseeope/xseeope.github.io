# Multi-period binomial pricing model

初始时刻是 $t=0$, 终止时刻是 $t=N$

市场上有三种资产，两个是基础资产，第三个是衍生资产：

* 无风险资产，也即政府债券，收益率 $r > 0$，定价过程表示为 $B: B_{t+1} = B_t(1+r)$

* 股票，初始价格为已知常数 $S_0$，定价过程表示为 $S:$

$$
S_{t+1}=
\begin{cases}
    uS_t\quad \text{with probability}\ \ 0<p<1\\
    dS_t\quad \text{with probability}\ \ 1-p
\end{cases}
$$

* 看涨期权，执行价格为 K，$t=N$ 时刻的价值为：$V_N = (S_N-K)^{+}$

---

Corollary (The simplified algorithm of the pricing and hedging)

Consider an $N-period$ binomial asset-pricing model, with $0 < d < 1 + r < u$. Let $V_N = F(S_N)$ be a random variable (a derivative security paying off at time N) depending only on the stock price $S_N$. For $n = N − 1,N − 2, · · · , 0$, define recursively backward in time the following sequence ofrandom variables

$$
V_{n}\left(S_{n}\right) =\frac{1}{1+r}\left[\tilde{p}V_{n+1}(uS_n)+(1-\tilde{p})V_{n+1}(dS_n)\right]
$$

Next define

$$
\Delta_{n}\left(S_{n}\right. )=\frac{V_{n+1}\left(u S_{n}\right)-V_{n+1}\left(d S_{n}\right)}{\left(u-d\right)S_{n}}
$$

If we set $X_0 = V_0$ and define recursively forward in time the portfolio values $X_1,X_2,\cdots,X_N$ by

$$
X_{n+1}=\Delta_n S_{n+1}+(1+r)(X_n-\Delta_n S_n)
$$

then we will have

$$
X_N(\omega_1,\cdots,\omega_N)=V_N(\omega_1,\cdots,\omega_N)\ for\ all\ (\omega_1,\cdots,\omega_N)\in\Omega
$$

Proof

$$
\begin{aligned}
    X_{n+1}(H)&=\Delta_n \mu S_{n}+(1+r)(X_n-\Delta_n S_n)\\
    &=(1+r)X_n + \Delta_n S_n (\mu - (1+r))\\
    &=(1+r)X_n + \frac{V_{n+1}\left(u S_{n}\right)-V_{n+1}\left(d S_{n}\right)}{\left(u-d\right)} (\mu - (1+r))\\
    &=(1+r)X_n + \tilde{q}V_{n+1}\left(u S_{n}\right) - \tilde{q}V_{n+1}\left(d S_{n}\right)\\
    &=\tilde{p}V_{n+1}\left(u S_{n}\right) + \tilde{q}V_{n+1}\left(d S_{n}\right)+\tilde{q}V_{n+1}\left(u S_{n}\right) - \tilde{q}V_{n+1}\left(d S_{n}\right)\\
    &=\tilde{p}V_{n+1}\left(u S_{n}\right) +\tilde{q}V_{n+1}\left(u S_{n}\right)\\
    &=V_{n+1}(H)
\end{aligned}
$$

similarly, we can get

$$
X_{n+1}(T)=V_{n+1}(T)
$$

we have

$$
X_{n+1}(\omega_1,\cdots,\omega_n,\omega_{n+1})=V_{n+1}(\omega_1,\cdots,\omega_n,\omega_{n+1})\ for\ all\ (\omega_1,\cdots,\omega_n,\omega_{n+1})\in\Omega
$$

therefore

$$
X_N(\omega_1,\cdots,\omega_N)=V_N(\omega_1,\cdots,\omega_N)\ for\ all\ (\omega_1,\cdots,\omega_N)\in\Omega
$$