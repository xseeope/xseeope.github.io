# RP_PCA

<font size = 5> **Factors That Fit the Time Series and Cross-Section of Stock Returns**</font>

<font size = 5> **Journal:**</font>

<font size = 4>

Review of Finanical Studies (2020.5)
</font>

<font size = 5> **Authors:**</font>

<font size = 4>

* Martin Lettau:
  
  Haas School of Business, University of California at Berkeley, NBER and CEPR
* Markus Pelger:
  
  Department of Management Science & Engineering, Stanford University
</font>

## Abstract

We propose a new method for estimating $\text{\color{red}{latent}}$ asset pricing factors that fit the time series and cross-section of expected returns. Our estimator generalizes principal component analysis (PCA) by including a penalty on the pricing error in expected returns. Our approach finds $\text{\color{red}{weak factors}}$ with high Sharpe ratios that PCA cannot detect. We discover five factors with economic meaning that explain well the cross-section and time series of characteristic-sorted portfolio returns. <mark>The out-of-sample maximum Sharpe ratio of our factors is twice as large as with PCA with substantially smaller pricing errors. Our factors imply that a significant amount of characteristic information is redundant. </mark>

<strong>“weak” factors:</strong>

* factors that affect only a subset of the underlying assets

* Weak factors are harder to detect than “strong” factors that affect all assets (“market” factor).

## Introducion

* Cochrane (2011), “factor zoo”:
  * which risk factors are important
  * which factors are subsumed by others

寻找可以同时解释共同运动（时间序列上）和预期收益横截面的因素的理论基础：
**APT认为: 系统的时间序列因素也决定了横截面风险溢价**

The RP-PCA method extracts five significant factors that together yield a high Sharpe ratio (SR), small pricing errors, and capture most of the time-series variation in the data.

## 1. Methodology

**假设:**

1. 超额收益遵循标准近似因子模型

2. 套利定价理论的假设条件得到满足

有了上述的假设，我们便可认为 N 个资产在 T 期的**超额收益率**满足如下形式 (latent factor structure)：

<span id="jump">

$$
X_{nt}=F_t\land_n^T+e_{nt}    \qquad  n=1,...,N, \quad t=1,...,T  \tag{2}
$$
</span>

$$
\iff \underbrace{X}_{T×N}=\underbrace{F}_{T×K}\quad\underbrace{\land^T}_{K×N}+\underbrace{e}_{T×N}
$$

在这里，我们需要估计两个部分：隐因子 F 和因子暴露 $\land（\beta）$

<font size = 5>**PCA vs RP_PCA**</font>

### 1.1 PCA method

PCA方法的目标函数：

$$
\text{PCA}: \qquad \hat{F}_{PCA}, \hat{\land}_{PCA} = \mathop{argmin}\limits_{\land,F}  \frac{1}{NT} \sum\limits_{n=1}^{N} \sum\limits_{t=1}^{T}  \big  ((X_{nt}-\overline{X}_n)-(F_t-\overline{F})\land_n^T \big)^2 \tag{3}
$$

这里是 $var(X) = E \big(X - E(X)\big)^2$ 的方差形式

$$
\boxed{\mathop{argmin}\limits_{F}  \frac{1}{NT} \sum\limits_{n=1}^{N} \sum\limits_{t=1}^{T}  \big  (X_{nt}-F_t\land_n^T \big)^2}
$$

对(3)式变形：

$$
\begin{array}{lll}
  \hat{F}_{PCA}, \hat{\land}_{PCA} & = & \mathop{argmin}\limits_{\land,F}  \frac{1}{NT} \sum\limits_{n=1}^{N} \sum\limits_{t=1}^{T}  \big  ((X_{nt}-F_t\land_n^T) - (\overline{X}_n-\overline{F}\land_n^T)\big)^2 \\
  & & \\
  & = & \mathop{argmin}\limits_{\land,F} \frac{1}{N}\sum\limits_{n=1}^{N}  E \big(e_{nt} - E(e_{nt})\big)^2 \\
  & & \\
  & = & \mathop{argmin}\limits_{\land,F} \frac{1}{N}\sum\limits_{n=1}^{N} var(e_{n})
\end{array}
$$

>[!TIP|label:TIP]
>
>$\qquad e_{nt} = X_{nt}-F_t\land_n^T$
>
>$\qquad E(e_{nt}) = e_n = E(X_{nt}-F_t\land_n^T) = \overline{X}_n-\overline{F}\land_n^T ，e_n$ 代表第 n 个资产在所有样本期 $t=1 \to T$ 的期望定价误差

Conventional statistical factor analysis applies PCA to the **sample covariance** matrix:

$$
\Sigma_X = \frac{1}{T}X^TX-\overline{X}*\overline{X}^T
$$

where $\overline{X}$ denotes the **sample mean** of excess returns

$$
\begin{bmatrix}
  {X_{11}}&{X_{21}}&{\cdots}&{X_{N1}}\\
  {X_{12}}&{X_{22}}&{\cdots}&{X_{N2}}\\
  {\vdots}&{\vdots}&{\ddots}&{\vdots}\\
  {X_{1T}}&{X_{2T}}&{\cdots}&{X_{NT}}\\
\end{bmatrix}_{T\times N}
$$

$\overline{X}_i = \frac{1}{T} \sum\limits_{j=1}^{T}X_{ji}$

$$
\overline{X} =
\begin{bmatrix}
  {\frac{1}{T}(X_{11}+X_{12}+\dots + X_{1T})}\\
  {\vdots}\\
  {\vdots}\\
  {\frac{1}{T}(X_{N1}+X_{N2}+\dots + X_{NT})}\\
\end{bmatrix}_{N\times 1}
$$

* 传统的PCA方法主要步骤如下:
  * 对资产收益率的 variance-covariance matrix $\Sigma_X$ 做特征分解，得到N个**互相垂直**的特征向量；
  * 选择前 K 个最大的特征值对应的特征向量作为等式(2)中因子载荷 $\land$ 的估计值：$\hat{\land}_{PCA} $，这 K 个特征向量表示将原收益率 X 所投影到的新空间的正交基；
  * 根据估计出的因子载荷 $\hat{\land}_{PCA} $，通过 OLS 回归，得到因子 F 的估计值：
  $$
  \hat{F}_{PCA}=X  \hat{\land}_{PCA}  (\hat{\land}^T_{PCA}  \hat{\land}_{PCA})^{-1}
  $$
  因子 F 也即 X 的主成分 (principal component)，特征向量对应的特征值就是因子 F 的方差

---

$$
\begin{aligned}
  \Sigma_X &= Q^Tdiag(\lambda_1，\lambda_2,\dots,\lambda_n)Q\\
  &\\
  & = \begin{bmatrix}
  {q_1^T}\\
  {q_2^T}\\
  {\vdots}\\
  {q_n^T}\\
\end{bmatrix}
\begin{bmatrix}
  {\lambda_1}&{0}&{\cdots}&{0}\\
  {0}&{\lambda_2}&{\cdots}&{0}\\
  {\vdots}&{\vdots}&{\ddots}&{\vdots}\\
  {0}&{0}&{\cdots}&{\lambda_n}\\
\end{bmatrix}
\begin{bmatrix}
  {q_1}&{q_2}&{\cdots}&{q_n}  
\end{bmatrix}
\end{aligned}
$$

>[!TIP|label:key point]
>- 大部分 PCA 做法是：假设 $E(X) = 0$，先对收益率矩阵 X demean，然后求协方差矩阵，此时 $\Sigma_X = \frac{1}{T}X^TX$<br>
>- 但如果 $E(X)$ 中包含了关于因子结构的信息，那么这一假设便是不合理的。基于此，RP_PCA方法放松了这一假设，以达到运用X的期望所包含信息的目的：
>$$\overline{X}=E[X] \not ={0} \\ \overline{F}=E[F] \not ={0} $$

### 1.2 RP_PCA method

#### 1.2.1 objective function

$$
\hat{F}_{RP}, \hat{\land}_{RP} = \mathop{argmin}\limits_{\land,F}  \underbrace{\frac{1}{NT} \sum\limits_{n=1}^{N} \sum\limits_{t=1}^{T} (X_{nt}-F_t\land_n^T)^2}_{\text{unexplained TS variation}}    +  \gamma \ \underbrace{ \frac{1}{N} \sum\limits_{n=1}^{N}(\overline{X}_n- \overline{F}\land_n^T)^2}_{\text{cross-section pricing error}}  \tag{4}
$$

与 PCA 类似，RP_PCA 方法通过最小化定价误差，求解线性隐因子模型中的 factor 和 loadings。$\gamma$ 代表平均截面定价误差在整个目标函数中的权重，这是 RP_PCA 方法和 PCA 方法的不同之处。$\gamma \geqslant -1 \ $ <i>[(proof)](#jump2)</i>

**通过考虑平均超额收益 $\overline{X}$ 和模型计算的平均超额收益的差值 $E[\hat{F}_{t}] \hat{B}^n_{t}$，相当于把横截面上的定价误差加入到最优目标函数中**

<details>
<summary>matrix-vector-form:</summary>

<table>
  <td id = "td1">
    $$\begin{bmatrix}
      {e_{11}}&{e_{21}}&{\cdots}&{e_{N1}}\\
      {e_{12}}&{e_{22}}&{\cdots}&{e_{N2}}\\
      {\vdots}&{\vdots}&{\ddots}&{\vdots}\\
      {e_{1T}}&{e_{2T}}&{\cdots}&{e_{NT}}\\
    \end{bmatrix}_{T\times N}$$</td>
  <td id = "td1"></td>
  <td id = "td1">➡️</td>
  <td id = "td1"></td>
  <td id = "td1">
    $$\begin{bmatrix}
      {}&{}&{}&{}\\
      {\overline{e_{1}}}&{\overline{e_{2}}}&{\cdots}&{\overline{e_{N}}}\\
      {}&{}&{}&{}\\
    \end{bmatrix}_{1\times N}$$</td>
</table>
</details><br>

>[!NOTE|label:NOTE]
> 原文中的 (4) 式可能表达有误，参考作者在另一篇关于 RP_PCA 的论文[《Estimating latent asset-pricing factors》](https://www.sciencedirect.com/science/article/pii/S0304407620300051)中给出的目标函数：<br>
> <br>
> 📘: We show that RP-PCA minimizes jointly the unexplained variation and pricing error:</p>

$$
\hat{F}_{RP}, \hat{\land}_{RP} = \mathop{argmin}\limits_{\land,F}  \underbrace{\frac{1}{NT} \sum\limits_{n=1}^{N} \sum\limits_{t=1}^{T} (\widetilde{X}_{nt} -   \widetilde{F}_t \land_n^T)^2}_{\text{unexplained TS variation}}    +  (\gamma+1) \ \underbrace{ \frac{1}{N} \sum\limits_{n=1}^{N}(\overline{X}_n- \overline{F}\land_n^T)^2}_{\text{cross-section pricing error}} \tag{5}
$$

where $\widetilde{X}_{t} = X_t - \overline{X}$, $\widetilde{F}_{t} = F_t - \overline{F}$

RP_PCA 的目标函数可以理解为：第一项是 PCA 的目标函数，也即[等式(2)](#jump)的OLS目标函数；第二项表示在PCA的基础上，将每个资产的定价误差 (n = 1,2, $\dotsb$ ,N) 先在时序上取均值，这些均值在截面上的定价误差。

<details class="details3">
<summary style="line-height: 1px; width: 6em">TIP:</summary>

这两项对于 X 和 F 的处理不一样，第一项将 X 和 F 进行 demean 处理，而第二项没有对 X和 F 进行 demean 处理，因此对二维随机变量 $e_{nt}$ 在时序上取期望后，$E(e_{nt}) = e_n$ 并不为0，根据 APT 的假设，$E\big(E(e_{nt})\big)  = E(e_n) = 0$，即对二维随机变量 $e_{nt}$ 在时序和截面上取两次期望后，其期望为0。

因此，RP_PCA目标函数第二项的完整形式：

$$
\begin{array}{ll}
  & \frac{1}{N} \sum\limits_{n=1}^{N}(\overline{X}_n- \overline{F}\land_n^T)^2\\
  & \\
  = & \frac{1}{N} \sum\limits_{n=1}^{N} \big((\overline{X}_n- \overline{F}\land_n^T) - E(\overline{X}_n- \overline{F}\land_n^T)\big)^2\\
  & \\
  = & \frac{1}{N} \sum\limits_{n=1}^{N} \big((e_n) - E(e_n)\big)^2\\
  & \\
  = & var(e_n)
\end{array}
$$

</details>

---

#### 1.2.2 objective matrix

求解等式 (5) 等价于对如下矩阵 $\Sigma_{RP}$ 应用 PCA 方法：

$$
\Sigma_{RP}=\frac{1}{T}X^TX + \gamma\overline{X}*\overline{X}^T \tag{6}
$$

* standard PCA using the variance-covariance matrix or the second-moment matrix is a special case of RP-PCA
* RP-PCA with $\gamma$>−1 can be understood as PCA applied to a matrix that $\mathbf{“overweights”}$ the means

different $\gamma$:

* $\gamma=0$, the RP-PCA objective is identical to the OLS objective function,  the OLS estimate $\hat{B}_n$ in Equation (9) is equal to the RP-PCA estimator $\hat{\land}_n$
* $\gamma=-1$, is similar to PCA, but in PCA  method $X_n$ and $\hat{F}$ are demeaned

<details class="details4">
<summary style="line-height: 9px; width: 23em">proof of equivalence between (5) and (6):</summary>

$$
\begin{bmatrix}
  {\overline{e_{1}}}&{\overline{e_{2}}}&{\cdots}&{\overline{e_{N}}}\\
\end{bmatrix}_{1\times N} = \frac{1}{T}1^{\top}XM_{\Lambda}
$$

(5) 式的第二项为：

$$
\frac{1}{N}(\frac{1}{T}1^{\top}XM_{\Lambda})(\frac{1}{T}1^{\top}XM_{\Lambda})^{\top} = \frac{1}{N} trace \left((\frac{1}{T}1^{\top}XM_{\Lambda})(\frac{1}{T}1^{\top}XM_{\Lambda})^{\top} \right)
$$

于是，(5) 式等价于：

<table style="font-size:15.0pt;line-height:18pt">
  <tr>
    <td id="td1l"></td>
    <td id="td1l">$\min \limits_{\Lambda,F} \frac{1}{NT} trace \left((\tilde{X}M_{\Lambda})^{\top}(\tilde{X}M_{\Lambda})\right)+(1+\gamma)\frac{1}{N}trace \left((\frac{1}{T}1^{\top}XM_{\Lambda})(\frac{1}{T}1^{\top}XM_{\Lambda})^{\top} \right)$</td>
  </tr>
  <tr>
    <td id="td1l">=</td>
    <td id="td1l">$\min \limits_{\Lambda} \frac{1}{NT} trace \left(M_{\Lambda}X^{\top}(I+{\frac{\gamma}{T}}1 1^{\top}) XM_{\Lambda}\right)$</td>
  </tr>
</table>

$$
\frac{1}{T}X^{\top}(I+{\frac{\gamma}{T}}1 1^{\top})X = \frac{1}{T}X^{\top}X + \gamma\overline{X}*\overline{X}^{\top}
$$

</details>

---

#### 1.2.3 estimate RP_PCA model

$$
X_{nt}=F_t B_n^T+e_{nt} \tag{9}
$$

等式(2)中的因子模型意味着没有截距项，因此残差 $e_{nt}$ 的期望不一定为0(截距项被包含在 $e_{nt}$ 中了)。
作为替代，我们可以利用等式(10)中的定价误差 $\alpha_n$ 来评估RP_PCA模型

$$
X_{nt}=\alpha_n+F_t B_n^T+e_{nt} \tag{10}
$$

等式(10)中，由于有了截距项 $\alpha_n$，则残差部分的信息被 $\alpha_n$ 吸收，此时残差 $e_{nt}$ 的期望为0，这里也假设了 $\alpha_n$ 的期望为0

>[!NOTE|label:提示]
>虽然OLS的时候对X和F进行了demean处理，$e_{nt}$ =0，但这只是为了用OLS来估计因子F。为了评估模型的好坏，我们需要用带有截距项的等式(10)，希望截距越接近0越好。而不是没有截距项的等式(9)

---

#### 1.2.4 A Summary for RP-PCA Method

<table>
  <tr>
    <td id = "td1">$\text{1.}$</td>
    <td id = "td1l">$\mathbf{对矩阵 \frac{1}{T}X^TX + \gamma\overline{X}*\overline{X}^T 应用PCA方法得到前K个主成分，作为因子载荷\land的估计，也即 \hat{\land}}$</td>
  </tr>
  <tr>
    <td id = "td1">$\text{2.}$</td>
    <td id = "td1l">$\mathbf{使用 \hat{\land} 在等式(9)中来估计因子: \hat{F}=X \hat{\land} (\hat{\land}^T  \hat{\land})^{-1}}$</td>
  </tr>
  <tr>
    <td id = "td1">$\text{3.}$</td>
    <td id = "td1l">$\mathbf{对于每个资产n，使用 \hat{F} 来估计等式(10)中的 \hat{\alpha} , \hat{B} 和 \hat{e}}$</td>
  </tr>
  <tr>
    <td id = "td1">$\text{4.}$</td>
    <td id = "td1l">$\mathbf{分别使用 \hat{\alpha} 和 \hat{e} 来估计 {RMS}_\alpha 和 \overline{\sigma}^2_e}$<br>
    </td>
  </tr>
  <tr>
    <td id = "td1"></td>
    <td id = "td1l">$\qquad {RMS}_\alpha = \sqrt {\hat{\alpha}^T\hat{\alpha}/N}$<br><br>
    $\qquad \overline{\sigma}^2_e = avg(Var(\hat{e}_n)/Var(X_n))$</td>
  </tr>
  <tr>
    <td id = "td1">$\text{5.}$</td>
    <td id = "td1l">$\mathbf{计算可以从估计出的潜在因子 \hat{F} 构建的最大\text{Sharpe Ratio}}$</td>
  </tr>
</table>

---

#### 1.2.5 Some proofs

>[!TIP|label:提示]
>$\gamma$为何从-1开始

协方差的定义：

$$
Cov(X,Y) = E[\big(X -E(X) \big) \big(Y -E(Y) \big)]
$$

$$
=E(XY) - E(X)E(Y)
$$

如果是总体协方差：

$$
Cov(X,Y) = \frac{1}{n} \sum\limits_{i=1}^{n} (x_i -\overline{x})(y_i -\overline{y})
$$

$$
=\frac{1}{n} \sum\limits_{i=1}^{n} x_i y_i - \overline{x}\ \overline{y}
$$

把X，Y都理解为n×1的向量，则：

$$
\frac{1}{n} \sum\limits_{i=1}^{n} x_i y_i - \overline{x}\ \overline{y}
$$

$$
=\frac{1}{n} \vec{X}^T \vec{Y} - \overline{X}\ \overline{Y}^T
$$

在PCA方法中，收益率矩阵 $X_{T×N}$ 是二维的，对其求协方差其实是消除时间 T 这一维度，因此 $X_{T×N}$ 的协方差为：

$$
\frac{1}{T} X^TX - \overline{X}*\overline{X}^T
$$

<span id="jump2">而RP_PCA想要利用一阶矩的信息，于是在PCA的目标矩阵后再加上m个由资产均值向量组成的矩阵，即：

$$
\begin{array}{ll}
  & \frac{1}{T} X^TX - \overline{X}\cdot \overline{X}^T + m \overline{X}\cdot \overline{X}^T \\
  & \\
  = & \frac{1}{T} X^TX + \text{\color{red}{(m-1)}} \overline{X}\cdot \overline{X}^T\\
  & \\
  = & \frac{1}{T} X^TX + \textcolor{red}{ \gamma}\ \overline{X}\cdot \overline{X}^T\\
\end{array}
$$

这里的 m-1 其实就是RP_PCA的目标矩阵中的参数 $\gamma$，$\gamma$ = m-1
由于RP_PCA想要在PCA的基础上再利用一阶矩的信息，因此给一阶矩的权重肯定为正，所以 $m \geqslant0$，所以 $\gamma \geqslant -1$

---

#### 1.2.6 estimating SDF

> <p id="p1">&nbsp;&nbsp; 📘: Lettau and Pelger (Forthcoming) show theoretically that the RP-PCA estimator is (asymptotically) more efficient than standard PCA in the sense that the stochastic discount factor (SDF) and factors estimated by RP-PCA are more highly correlated with the true SDF and factors than those estimated by PCA.</p>

得到 F 的估计量后，我们可以估计 SDF：

* 根据F的数据，计算以这些因子为测试资产构造的有效前沿的最大夏普比率：

<font size = 4> $\hat{b}_{MV} = \Sigma_{F}^{-1} \mu_F$ </font> $\quad$(其中$\mu_F$和$\Sigma_{F}^{-1}$ 分别代表 $\hat{F}$ 的期望向量和协方差矩阵)

* 如果 $\Sigma_{F}$ 是对角矩阵，则：<font size = 4> $\hat{b}_{MV,i} = \cfrac{\mu_{F,i}}{\sigma^2_{F,i}} $ </font>

* 由此可以得到SDF：<font size=4> $M_t = 1 - \hat{b}_{MV}^T(\hat{F}_T - E[\hat{F}_T]) $ </font>

### 1.3 Properties of RP-PCA

#### 1.3.1 ‘strong factors’ and 'weak factors'

Lettau and Pelger认为，对因子的估计，取决于因子的“**信号强度**”相对于特质性风险，也即 “噪声” 方差的大小。RP_PCA方法将一阶矩的信息纳入进来，提高了因子的信号强度，从而提高了**信噪比**

**通过对因子载荷的适当标准化，因子的强度取决于载荷 $\beta$ 的结构 $\land$**

* 在一个全部都是“强因子”的模型中，$\land^T\land/N \stackrel{p}{\rightarrow}  I_K$

* 在一个全部都是“弱因子”的模型中，$\land^T\land \stackrel{p}{\rightarrow}  I_K$

>[!NOTE|label:提示]
>根据前面的分析，因子的载荷是由$\Sigma_X$的前K个特征值对应的特征向量组成，这些向量互相之间正交，因此不难理解$\land^T\land$是一个对角矩阵，再进行相应的标准化，可以近似单位矩阵$\\$“弱因子”只在一部分资产上的载荷显著不为0，因此某一“弱因子”在所有测试资产上的载荷平方和肯定很小，所以其协方差矩阵不用除以N便可近似为单位矩阵

**一般的模型同时包含“强因子”和“弱因子”，因此，若运用PCA方法直接对 $\Sigma_X$ 进行分解，那么：**

* "强因子"由于方差较大，其特征值相应很大，因此会被选为"主成分"；

* “弱因子”由于方差较小，其特征值相应很小，可能不会被选为“主成分”，这会对估计造成偏误

**作者认为：因子的“信号强度”相对于特质性风险的大小，有一个阈值(threshold),**

* 如果低于这个阈值，那么这个因子很难用PCA或RP_PCA方法检测到；
* 如果高于这个阈值，那个这个因子能被检测到，且它与现实市场中某个因子的会有很高的相关性
  
RP_PCA方法中，通过改变参数 $\gamma$ 的大小，可以提高因子的强度，使得“弱因子”更容易被检测到，整体的估计相对于PCA方法也更精确。此外，阈值 (threshold) 的大小和 $\gamma$ 无关，因此可以通过改变 $\gamma$，使得因子的强度发生变化。

**对不同数据的分析结果如下：**

* 对“强因子”的估计：强因子可以用基于PCA的方法可靠地估计，且它们与 $\gamma$ 的选取无关

* 对“弱因子”的估计：

  * 即使N和T增长，弱因子也只能被有偏差地估计
  
  * 如果一个因子的信号强度低于阈值，则根本无法检测到；只有通过改变 $\gamma$ 的取值，才可能被检测到
  
  * 存在一个有限的 $\gamma$ ，使得估计出的因子与真实因子的相关性最大，并且只要 $\gamma$ >−1,其估计出的因子与真实因子的相关性大于用PCA方法得到的结果

#### 1.3.2 How should the optimal $\gamma$ be chosen?

**简要来说，$\gamma$ 的选取有如下三条参考标准：**

1. 一个非常大的 $\gamma$ 能最大化检测到弱因子的概率，但同时会降低其与真实因子的相关性
2. 如果 $\gamma$ 选取的非常大，会造成样本外表现的恶化
3. 实证的做法：$\gamma$ 从-1开始增大，直到样本外表现不再提升

<strong>

对于Sharpe Ratio为正的因子：
$\gamma$ 较小时，随着 $\gamma$ 的增加，估计因子和真实因子的相关性快速增加，$\gamma$ 增加到一定程度时，相关性不会因为 $\gamma$ 的增加继续提升

对于Sharpe Ratio为0的因子：
$\gamma$ 越大，估计因子和真实因子的相关性反而会降低，此时最优 $\gamma$ 为-1，因为均值为0的因子，其均值不包含任何有用的信息，此时较高的 $\gamma$ 会增加对无信息横截面误差的权重
</strong>

<div align='center'>

![](RP_PCA-figures/figure1.png)
</div align='center'>

**Figure 1
Weak factors: Correlation of estimated factor with the true factor** $\\$
This plot shows the correlation of the estimated factor with the true factor as a function ofγ for different parameter
settings implied by the theoretical results of the weak factor model (N=370 and T =650).

对于同一条线（Sharpe Ratio相同），$\gamma$ 越大，代表给均值信息赋予的权重越大，那么相关性也会越大

对于同一条线（Sharpe Ratio相同），但不同的方差（上下两图），可以发现方差越大时，其与真实因子的相关性越大

## 2. Empirical Results

<table>
  <th id="th1c" colspan=2>模型评价指标</th>
  <tr>
    <td id="td1l">SR</td>
    <td id="td1l">maximum Sharpe ratio that can be obtained<br> by a linear combination of the factors</td>
  </tr>
  <tr>
    <td id="td1l">$RMS_{\alpha} \qquad \qquad$</td>
    <td id="td1l">the root-mean-square pricing error</td>
  </tr>
  <tr>
    <td id="td3l">$\overline{\sigma}^2_e$</td>
    <td id="td3l">the average idiosyncratic variance</td>
  </tr>
</table>

factor 和 loadings 是在20年(T=240)的**滚动窗口**中估计的，利用这些估计的载荷，包括截至时间 T 的信息，可以预测 T+1 的收益，并计算 T+1 时的样本外定价误差

当展示实证结果时，将因子的协方差矩阵标准化更有用，即 $\Sigma_F = I_K$，这是因为当比较不同的因子模型时，因子载荷必须是可比较的。

整体模型不受任何标准化的影响

### 2.1 Double-sorted portfolios

共有八组数据，每一组数据都是经过双重排序后，由25个投资组合构成的新组合<br>
这里比较了RP_PCA、PCA、FF3三种模型的**样本外估计结果**

![](RP_PCA-figures/table1.png)

**结果分析：**

在八种情况中，有六种情况下，RP_PCA的Sharpe Ratio大于PCA和FF3的Sharpe Ratio，且RP_PCA的 $RMS_\alpha$ 最小，此外，RP_PCA 在样本外残差方面的表现也更好

**不同的PCA方法可能会影响因子被选择的顺序，** 以size/short-term reversal这组资产为例:

* 在RP_PCA方法中，对这组资产提取的第二个因子是 reversal factor，第三个因子是 size factor；

* 而在PCA方法中，对这组资产提取的第二个因子是 size factor，第三个因子是 reversal factor;

**原因是 reversal factor 捕获了平均收益差异的信息，因此在RP_PCA估计中被赋予了更高的权重**

---

![](RP_PCA-figures/figure2.png)

**Figure 2
Out-of-sample results as a function of $\gamma \\$**
Out-of-sample maximal Sharpe ratios, root-mean-squared pricing errors, and unexplained idiosyncratic variation
for different number of factors and $\gamma$. **Left: Size/Accrual. Right: Size/Short-Term Reversal.**

对 Size/Accrual 这一组资产来说，当加入第三个因子的时候，样本外SR大幅提升，且样本外  $RMS_\alpha$ 大幅降低；
对 Size/Short-Term Reversal 这一组资产来说，当加入第四个因子的时候，样本外SR大幅提升，且样本外 $RMS_\alpha$ 大幅降低；

不论因子的个数，当 $\gamma$ 从-1开始增加时，样本外SR逐渐提升，且样本外 $RMS_\alpha$ 逐渐降低

<hr align = "center" width="90%" size = 5 color = 'lightgreen'/>

![](RP_PCA-figures/figure3.png)

**绿色代表因子载荷为正，红色代表因子载荷为负**

对 Size/Accrual 这一组资产来说，RP_PCA和PCA的前两个因子很像

第一个factor是一个“long” factor，所有投资组合都具有正的载荷，并且小股票组合的载荷更大，这类似于 market factor

第二个factor是一个long-short factor，小股票投资组合的因子载荷为负，大股票投资组合的因子载荷为正，这类似于FF3中的 SMB

第三个 RP_PCA factor：高应计项目的公司载荷为负，低应计项目的公司载荷为正，类似于Fama-French类型的因子

第三个 PCA factor：没有明显的表征

对 Size/Short-Term Reversal 这一组资产来说，实验结果与前面的分析基本吻合

### 2.2 Large cross-section of single-sorted portfolios

数据:
<font size = 4>

* single-sorts of 37 different characteristics
* The sample span is November 1963 to December 2017 in all cases
</font>

将每个特征分别按10分位数分为10组，则共有370个test portfolios。由于大多数相关信息都包含在每个特征的第一个和第十个十分位数的投资组合中，因此，我们考虑了一个较小的横截面，将37个 decile-1 和 37个decile-10 投资组合作为测试基准。(full panel of 370 portfolios on the Online Appendix)

<div align='center'>

![](RP_PCA-figures/figure4.png)
</div align='center'>

**如何判断哪些因子是系统性的，哪些因子是特质性的**

>[!TIP|label:reference]
>Onatski criterion: Alexei Onatski, Chen Wang.SPURIOUS FACTOR ANALYSIS.Econometrica

* $\gamma$<10的时候，在两个样本中，第五个factor的eigenvalue difference都低于临界值，表明此时前四个因子是系统性因子

* $\gamma \geqslant$10的时候,在两个样本中，第五个factor的eigenvalue difference都高于临界值，表明此时前五个因子是系统性因子

**这表明第五个因子是弱因子，需要通过调整RP_PCA中的参数 $\gamma$ 才能被检测到**

对比图A和图B可以发现，74个十分位数组合和全样本组合，检测出的系统性因子基本一致，证明**大部分相关信息的确保留在37个 decile-1 和 37个decile-10 投资组合中**

<hr align = "center" width="90%" size = 5 color = 'lightgreen'/>

**cross-validation estimation（交叉验证）**

验证不同参数 $\gamma$ 和不同因子个数K的组合

方法：将样本分为三个数据量相同的子样本 $v_1,v_2,v_3$，使用其中一个子样本的数据来估计模型，并用另外两个子样本的数据来评估样本外表现，并将三次样本外的数据进行平均

**黄色表示低Sharpe Ratio，红色表示高Sharpe Ratio**

<div align='center'>

![](RP_PCA-figures/figure5.png)
</div align='center'>

同样证实五个系统性因子

---

![](RP_PCA-figures/figure6.png)

前五个因子的样本外Sharpe Ratio逐渐增加，但添加其他因子对样本外SR的影响很小，这证实了RP_PCA提取了五个系统性因子

---

![](RP_PCA-figures/table2.png)

之所以FF3和FF5模型在个股上表现得更好，是因为，PCA和RP_PCA都假定公司特征是不随时间变化的，而个股的特征变化非常大；FF模型则是直接将收益率回归到特征上来，其内在逻辑是个股收益率和特征都是随时间变化，因此需要找到它们之间的相关性，也即这些特征的 factor loading

### 2.3 Individual stocks

数据：

* a balanced panel of stock returns from May 1972 to December 2013
* N=270 stocks with T =500 monthly returns (CRSP)
  
![](RP_PCA-figures/figure7.png)

可以看到，当研究对象是个股而不再是投资组合时，RP_PCA方法和PCA方法的样本内表现均不如它们应用于投资组合时，且RP_PCA方法的样本外表现更差，SR非常低，且 $RMS_\alpha$ 较高

造成这种现象的原因可能如下：

* RP_PCA方法和PCA方法都假设因子载荷时不变，这一假设对于投资组合来说尚可，但对于个股来说不再适用
* 个股收益的波动性远远大于投资组合，使得对个股均值的估计十分不精确。而RP_PCA方法又考虑了均值的信息，因此它所使用的信息可能本就有误，这也是它样本外表现差于PCA方法的原因
* 个股收益的信噪比低于投资组合的信噪比，这使得共同因子的识别更加困难
* 个股的因子结构可能不如投资组合稳定

---

![](RP_PCA-figures/figure8.png)

**Generalized correlations between loadings estimated on the whole sample and rolling windows with lengths of 240 months.**

>[!NOTE|label:注意]
>不是和真实因子的correlation

---

补充：

In PCA, the eigenvalues are equal to factor variances, while eigenvalues in RP-PCA are equal to a more generalized notion of “signal strength” of a factor that is defined later.

---

## 3. Replication

RP_PCA 实证结果：

<table>
  <tr>
    <th id="th1" rowspan="2"></td>
    <th id="th2c" colspan="2">$SR$</th>
    <td id="td2"></td>
    <td id="th2c" colspan="2">$RMS_{\alpha}$</th>
    <td id="td2"></td>
    <td id="th2c" colspan="2">$\bar{\sigma}_e$</th>
  </tr>
  <tr>
    <td id="td3c">RP-PCA</td>
    <td id="td3c">PCA</td>
    <td id="td3"></td>
    <td id="td3c">RP-PCA</td>
    <td id="td3c">PCA</td>
    <td id="td3"></td>
    <td id="td3c">RP-PCA</td>
    <td id="td3c">PCA</td>
  </tr>
  <tr>
    <td id="td1l">SIZE&BM25</td>
    <td id="td1c">0.24</td>
    <td id="td1c">0.23</td>
    <td id="td1"></td>
    <td id="td1c">0.18</td>
    <td id="td1c">0.18</td>
    <td id="td1"></td>
    <td id="td1c">7.64%</td>
    <td id="td1c">7.63%</td>
  </tr>
  <tr>
    <td id="td1l">SIZE&ACCRUAL25</td>
    <td id="td1c">0.29</td>
    <td id="td1c">0.19</td>
    <td id="td1"></td>
    <td id="td1c">0.10</td>
    <td id="td1c">0.13</td>
    <td id="td1"></td>
    <td id="td1c">6.97%</td>
    <td id="td1c">6.77%</td>
  </tr>
  <tr>
    <td id="td1l">SIZE&INV25</td>
    <td id="td1c">0.31</td>
    <td id="td1c">0.27</td>
    <td id="td1"></td>
    <td id="td1c">0.14</td>
    <td id="td1c">0.16</td>
    <td id="td1"></td>
    <td id="td1c">7.11%</td>
    <td id="td1c">7.18%</td>
  </tr>
  <tr>
    <td id="td1l">SIZE&MOM25</td>
    <td id="td1c">0.24</td>
    <td id="td1c">0.23</td>
    <td id="td1"></td>
    <td id="td1c">0.19</td>
    <td id="td1c">0.21</td>
    <td id="td1"></td>
    <td id="td1c">7.93%</td>
    <td id="td1c">8.04%</td>
  </tr>
  <tr>
    <td id="td1l">SIZE&OP25</td>
    <td id="td1c">0.18</td>
    <td id="td1c">0.19</td>
    <td id="td1"></td>
    <td id="td1c">0.12</td>
    <td id="td1c">0.12</td>
    <td id="td1"></td>
    <td id="td1c">8.55%</td>
    <td id="td1c">8.71%</td>
  </tr>
  <tr>
    <td id="td3l">SIZE&STREV25</td>
    <td id="td3c">0.20</td>
    <td id="td3c">0.16</td>
    <td id="td3"></td>
    <td id="td3c">0.20</td>
    <td id="td3c">0.21</td>
    <td id="td3"></td>
    <td id="td3c">7.64%</td>
    <td id="td3c">7.62%</td>
  </tr>
</table>

![](RP_PCA-figures/figure2_new.png)

![Figure2](RP_PCA-figures/figure2_new1.png)

![Figure2](RP_PCA-figures/figure2_new2.png)

![1696669739920](image/RP_PCA/1696669739920.png)