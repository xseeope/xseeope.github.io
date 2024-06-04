# HW of Fama-Macbeth

## So What is Fama-Macbeth reg???

- 1973年提出，目的是检验CAPM
- 两步**截面**回归，可以排除残差在截面上的相关性对标准误的影响
- 在金融领域，这个回归常被用于在多因子模型中分析投资标的截面预期收益率与因子暴露的关系
- Two- pass regression estimate

## Show me formula!!

### Step1

对单个股票的时间序列做如下回归，得到个股收益率在因子上的暴露$\beta_i$ d s s s s s s s s s s s
$$
R_{it}=\alpha_i+\beta_i'f_t+\varepsilon_{it}
$$
这里的因子 $f$ 可以是随便什么东西，可以是某个特殊组合的收益率，也可以是宏观指标等。

上面这个回归有些比较显然的事实：

- 第一步回归的残差是与$i,t$有关的，说的是$i$股票回归后在$t$时刻的残差
- 回归得到的$\alpha_i,\beta_i$都是与时间无关，可以理解是股票$i$的一个固有属性

### Step2

第二步做了如下的截面回归：

$$
R_{it}=\beta_i'\lambda_t+\alpha_{it}\\
矩阵形式：\\
R_t=\beta'\lambda_t+\alpha_t\\
R_t:N\times1,\quad
\beta:K\times N,\quad
\lambda:K\times1,\quad
\alpha_t: N\times1
\\
\hat{\lambda}=\frac{1}{T}\sum\limits_ {t=1}^T\hat{\lambda_t}\\
\hat{\alpha}_i=\hat{\lambda}=\frac{1}{T}\sum\limits_ {t=1}^T\hat{\alpha}_{it}
$$

注意下，Fama-Macbeth的这个回归是在每一个 t 都做了一次**截面**回归，也就是说每一个 t 时刻固定的情况下回归出一个 $\lambda_t$ 和 $\alpha_{it}$ ,然后在把他们取均值。

- 做平均之前的估计出的estimators含义
  - 该回归是 t 时刻截面上的100家公司的收益回归到他们的固有属性，which is因子暴露上
- 这里 t 时刻的$\lambda_t$表示的其实是一个斜率，即SML的斜率，怎么解释呢？其实我们知道在 t 时刻这个截面上，有很多支股票，有个显然的事实是每个股票的 $\beta$ 都是不一样的，当然他们的收益也是不一样的，然后我们又假定了 $\beta$ 与收益的关系是线性的，那么这个回归出的 $\lambda_t$ 就会是个斜率，代表了在 t 时刻，收益率与 $\beta$ 的一个关系，虽然每个公司的 $\beta$ 都不一样，但是还是可以总结为有 K 种 $\beta$ ，所以相应的，会有 K 个 $\lambda_t$ 。