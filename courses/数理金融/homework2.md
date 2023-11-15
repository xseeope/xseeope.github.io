# 数理金融作业2

**证明一个只在企业破产时得到 1 元的资产，在 0 时刻的价值为：$(\dfrac{x}{\delta_b})^{r_-}$**

$\color{orange}{\mathbf{\Large{Answers:}}}$

现金流满足如下分布：

$$
\mathrm{d}X_t=\mu X_t\mathrm{d}t+\sigma X_t\mathrm{d}W_t
$$

对于任意时刻 s，s>t:

$$
X_s=X_t e^{\left(\mu-\frac{1}{2}\sigma^2\right)\left(s-t\right)+\sigma\left(W_s-W_t\right)}
$$

t 时刻的价值 $V(X_t)$ 满足：

$$
V\left(x_{t}\right)=E_{t}^{Q}\left[\int_{t}^{\tau_{d}}e^{-r\left(s-t\right)}\left(a X_{x}+K\right)d s+e^{-r\left(\tau_{d}-t\right)}g\left(x_{d}\right)\right]
$$

对于一个只在企业破产时得到 1 元的资产：

$$
\begin{cases}
   a =0  \\
   K = 0 \\
   g\left(x_{d}\right) = 1
\end{cases}
$$

于是：

$$\begin{aligned}
\lim_{x_{t}\to+\infty}V\left(x_{t}\right) \qquad&=\qquad \lim_{\tau_d \to+\infty}E_{t}^Q\left[\int_{t}^{\tau_{d}}e^{-r\left(s-t\right)}\left(a X_s+K\right)d s+e^{-r\left(\tau_d-t\right)}g\left(x_{d}\right)\right]\\
\\
&=\qquad E_{t}^{Q}\left[\int_{t}^{+\infty}e^{-r\left(s-t\right)}\left(a X_{s}+K\right)d s\right] \\
\\
&=\qquad \int_{t}^{+\infty}e^{-r\left(s-t\right)}\left(a E_{t}^{Q}X_{s}+K\right)ds\\
\\
&=\qquad \frac{a x_{t}}{r-\mu}+\frac{K}{r}\\
\\
&=\qquad 0
\end{aligned}$$

$$
\therefore \ V(x_t)=A_1x_t^{\gamma_+}+A_2x_t^{\gamma_-}+\frac{ax_t}{r-\mu}+\frac{K}{r}=A_1x_t^{\gamma_+}+A_2x_t^{\gamma_-},\quad x_t\in\mathcal D
$$

又：

$$
\lim_{x_t\rightarrow\infty}V(x_t)=A_1x_t^{r_+}+A_2x_t^{r_-}=0 \tag{1}
$$

$\because r_+ > 1, \therefore A_1 = 0$<br>
企业破产时，投资者得到1元，也即 $x_t = \delta_b$ 时，$V(x_t)=1$

$$
V(\delta_b) = A_2 \delta_b^{r_-}=1
$$

解得：$A_2 = \delta_b^{-r_-}$，代入(1)式得：

$$
V(x_t)=A_2x_t^{r_-}=(\dfrac{x_t}{\delta_b})^{r_-}
$$

因此一个只在企业破产时得到 1 元的资产，其在 0 时刻的价值为：$(\dfrac{x}{\delta_b})^{r_-}$