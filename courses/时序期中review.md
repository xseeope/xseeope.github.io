# 时序期中review



参考资料https://www.math.pku.edu.cn/teachers/lidf/course/stochproc/stochprocnotes/html/_book/sptypes.html

### 第一章

**白噪声定义：**

White noise $\begin{Bmatrix}a_t\end{Bmatrix}$
$$
E(a_t)=0 \quad Var(a_t)=\sigma^2 \quad \gamma_k=0 \; for\;k\neq0
$$


**白噪声检验**：Q-test等

**信息准则：**

**正态分布检验：**

**ACF**：关于滞后期的函数，只对平稳的序列有用

**PACF：**如$PACF(3,3)$的检验，要得到三个方程的方程组，这三个方程通过对用于拟合的模型两边乘以$X_{t-1},X_{t-2},X_{t-3}$，

**ADF，PP，与KPSS检验单位根：**不等价，KPSS更powerful，KPSS原假设为不存在单位根，ADF，PP的原假设为存在单位根

**平稳性定义（宽平稳：**

如果$X(t)$是二阶矩过程（二阶矩对于所有$t$都存在则为二阶矩过程），并且$E[X(t)]=\mu$（不依赖于$t$），协方差函数$\gamma(t,s)$只与时间差$t-s$有关，则称${\{X(t), t\in T\}}$为宽平稳或二阶平稳过程，

**严格平稳：**

如果随机过程${\{X(t), t\in T\}}$ 对任意的$t_1,\dots,t_n \in T$和任意的$h$（使得$t_i+h\in T$），$(X(t_1+h),\dots,X(t_n+h))$与$(X(t_1),\dots,X(t_n))$有相同的联合分布记为
$$
(X(t_1+h),\dots,X(t_n+h)) \stackrel{d}{=} (X(t_1),\dots,X(t_n))
$$

则称${\{X(t), t\in T\}}$ 为严平稳的


### 第二三四章

pacf：等价于相关系数（小于1）

|          |    MA    |    AR    |   ARMA   | 单位根 |
| :------: | :------: | :------: | :------: | :----: |
| **ACF**  |  cutoff  | 指数衰减 | 指数衰减 |        |
| **PACF** | 指数衰减 |  cutoff  | 指数衰减 |        |
| **IRF**  |  cutoff  | 指数衰减 | 指数衰减 |        |

对于AR过程，$PACF(3)=\psi_3$

$AR(p)$模型平稳性判断：
$$
\begin{vmatrix}\varphi_p<1\end{vmatrix} \qquad
1-\varphi_1-\cdots-\varphi_p\neq0
$$
对于$AR(2)$特征方程所有根在单位圆外充要条件：
$$
\begin{vmatrix}\varphi_p<2\end{vmatrix} \qquad
\varphi_2\pm\varphi_1<1
$$

### 第五章

**单位根检验：**如何下结论（必考



### 第六章VAR

**VAR平稳性条件：**

对于一个$VAR(p)$模型：$r_t=\phi_0+\Phi_1r_{t-1}+\cdots+\Phi_pr_{t-p}$其稳定性条件为方程：
$$
\begin{vmatrix}I-\Phi_1x-\Phi_2x^2-\cdots-\Phi_px^p\end{vmatrix}=0
$$
的所有根在单位圆外

互协方差矩阵（Cross-covariance matrix）$\pmb{\Gamma_l}$

Both $E(X_t),Cov(X_t,X_{t-j})$  are time invariant.其中：
$$
E(X_t)=\begin{bmatrix}E(x_{1t})\\E(x_{2t})\end{bmatrix}=\mu
\\
\\Cov(X_t,X_{t-l})=\begin{bmatrix}Cov(x_{1t},x_{1,t-l})&Cov(x_{1t},x_{2,t-l})\\Cov(x_{2t},x_{1,t-l})&Cov(x_{2t},x_{2,t-l})\end{bmatrix}=\Gamma_l
\\
\\\Gamma_l = E[(X_t-\mu)(X_{t-l}-\mu)']
$$
需要注意如果$l\neq0$时互协方差矩阵$\pmb{\Gamma_l}$是非对称的（symmetric )，可以这样理解：
$$
\pmb{\Gamma_l}=\begin{bmatrix}
								\Gamma_{11}(l) & \Gamma_{12}(l)
							\\\Gamma_{21}(l) & \Gamma_{22}(l)
\end{bmatrix}
$$
$\Gamma_{12}(l)$表示的是$x_1$受到$x_2$的历史信息的影响，而$\Gamma_{21}(l)$表示的是$x_2$受到$x_1$的历史信息的影响，这两个影响水平没有理由非得相等，所以不能说互协方差矩阵$\pmb{\Gamma_l}$是对称的。

互相关矩阵（Cross-correlation matrix）$\pmb{\rho_l}$
$$
\pmb{D}=\begin{bmatrix}
  std(x_{1t}) & 0
\\0 & std(x_{2t})
\end{bmatrix}=
\begin{bmatrix}
  \sqrt{\Gamma_{11}(0)} & 0
\\0 & \sqrt{\Gamma_{22}(0)}
\end{bmatrix}
\\
\\
\pmb{\rho_l=D^{-1}\Gamma_lD^{-1}}
$$
$\rho_{ij}(l)$表示的含义为$x_{it}$与$x_{j,t-l}$之间的相关系数，且如果有平稳性，则存在如下性质：
$$
\pmb{\Gamma_l=\Gamma_{-l}'}\qquad\pmb{\rho_l=\rho_{-l}'}
$$
这是因为：$corr(x_{1t},x_{2,t-l})=corr(x_{1,t+l},x_{2t})$，而这个等式成立是因为相关系数交换顺序其值不变和平稳性。



**格兰杰因果关系：**

什么对什么有格兰杰因果关系别写反了

**VAR模型定阶：**信息准则

**向量白噪声检验：**

多元Q-test，Ljung-Box $Q_k(m)$统计量服从$\mathcal{X_{k^2m}^2}$分布，$k$为时间序列的数量
$$
H_0:\pmb{\rho_1=\cdots=\rho_m=0}
$$
原假设含义为原本的数据都是独立的，因此在p值较小时因拒绝原假设（p值含义$H_0$为真时拒绝$H_0$的概率，因此当其足够小时，我们有很大的信心去拒绝$H_0$，并且此时$H_0$也确实为假

### 第七章（不考）

### 第八章

**协整定义：**存在线性组合使得不平稳的不同分量变换后平稳

**协整的检验：**

**VECM定义：**

**VAR转换为VECM的表达：**做一阶差分再做新的系数矩阵$\Psi-I$的分解，VECM阶数将会是VAR的阶数减1




