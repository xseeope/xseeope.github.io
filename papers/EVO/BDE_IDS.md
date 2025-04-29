# A Bidirectional Differential Evolution-Based Unknown Cyberattack Detection System

IEEE Transactions on Evolutionary Computation, 2025

- Sichuan University
- Institute of Information Engineering, Chinese Academy of Sciences

## Introduction
本文旨在构建一个可以监控到已知和未知的攻击的 IDS（Intrusion Detection System）。本系统被类比与人工智能免疫系统 AIm-based IDSs（Artificial Immunity），可以识别自身抗原（self antigens 对应 normal data）与非自身抗原（nonself antigens 对应 abnormal data），并在面对未知的 antigen 时，可以自我演化出对应的 detector。

## Related Works and Challenges
![](/pics/BDE_IDS_fig1.png)

## Preliminaries
### A. Basic Elements of AIm-based IDS
**抗原 Antigen** 
每一个样本都被表示为一个 $n_d$ 维的点，其中正常与异常点分别被映射为自身抗原与非自身抗原（self antigens and nonself antigens），形式化表达如下：
$$
\left\{\begin{array}{l}
\mathbf{S}_{\mathrm{tr}}=\left\{\boldsymbol{g}_{\mathrm{s}}^{(i)}\left|\mathbf{g}_{\mathrm{s}}^{(i)}=\left(g_{\mathrm{s}}^{(i, 1)}, g_{\mathrm{s}}^{(i, 2)}, \ldots, g_{\mathrm{s}}^{\left(i, n_{\mathrm{d}}\right)}\right), i=1,2, \ldots,\left|\mathbf{S}_{\mathrm{tr}}\right|\right\}\right. \\
\mathbf{N}_{\mathrm{tr}}=\left\{\boldsymbol{g}_{\mathrm{ns}}^{(j)}\left|\boldsymbol{g}_{\mathrm{ns}}^{(j)}=\left(g_{\mathrm{ns}}^{(j, 1)}, g_{\mathrm{ns}}^{(j, 2)}, \ldots, g_{\mathrm{ns}}^{\left(j, n_{\mathrm{d}}\right)}\right), j=1,2, \ldots,\left|\mathbf{N}_{\mathrm{tr}}\right|\right\}\right.
\end{array}\right.
$$
其中 $|\mathbf{N}_{tr}|$ 与 $|\mathbf{S}_{tr}|$ 分别为自身抗原与非自身抗体集合的势。 $\mathbf{S}_{tr} \cap \mathbf{N}_{tr} = \emptyset$。

**自区域与自半径 Self Region and Self Radius**
对于每一个 self antigen $\mathbf{g}^{(i)}_{s}$ 都有一个对应的自区域 self region $\mathbf{R}^{(i)}_{s}$，这些自身抗原的总和可以写为：
$$
\mathbf{R}_{\mathrm{s}}=\bigcup_{i=1}^{\left|\mathbf{S}_{\mathrm{tr}}\right|} \mathbf{R}_{\mathrm{s}}^{(i)} .
$$
当一个点 $\mathbf{q}$ 落在 $\mathbf{R}_{s}$ 中时（$\mathbf{q} \in \mathbf{R}_{s}$），则 $\mathbf{q}$ 会被判断为一个自身抗原 self antigen。$\mathbf{g}^{(i)}_s$ 的覆盖（coverage）为一个超球面，球面半径为自半径 self radius，记作 $r_{s}$。

**Detector**
对于 nonself antigens 同样存在一个超球面 $r_{ns}$：
$$
r_{\mathrm{ns}}=\min _{\boldsymbol{g}_{\mathrm{s}}^{(i)} \in \mathbf{S}_{\mathrm{tr}}}\left\|\boldsymbol{g}_{\mathrm{ns}}-\boldsymbol{g}_{\mathrm{s}}^{(i)}\right\|_2-r_{\mathrm{s}}
$$
对于单独的一个 nonself antigen，其存在一个对应的 detector，记为 $\mathcal{D}_{ns}(\mathbf{g}_{ns}, r_{ns})$，如果用于测试的 antigen 掉落在 detector 的范围内，则其将会被判断为 nonself antigen。

### B. Differential Evolution Algorithm
DE 算法主要包含三个部分，突变，交叉和选择。

**突变 Mutation**
使用 DE/current-to-best/1 策略：
$$
\boldsymbol{x}_{\mathrm{mu}}(t)=\boldsymbol{x}_{\mathrm{r}}(t)+\lambda \times\left[\boldsymbol{x}_{\text {best }}-\boldsymbol{x}_{\mathrm{r}}(t)\right]+\mu \times\left[\boldsymbol{x}_{\mathrm{r}_1}(t)-\boldsymbol{x}_{\mathrm{r}_2}(t)\right] .
$$
其中 $\boldsymbol{x_{r_1}}(t)$ 和 $\boldsymbol{x_{r_2}}(t)$ 为两个从当前种群中随机选择的父代，$\boldsymbol{x_{best}}$ 为当前种群中的最佳个体，$\lambda$ 和 $\mu$ 为两个超参数，作为缩放因子。

**交叉 Crossover**
将突变个体与其父代个体进行组合，生成用于测试的个体，本文使用 binomial crossover 策略。

**选择 Selection**
选择比父代更合适的个体。

## Proposed BDE-IDS

### A. Clustering of Self Antigens
使用 [Min-Max](https://en.wikipedia.org/wiki/Feature_scaling) 对原始数据归一化后，对 self antigens 进行 k-means 聚类，记为 $\mathbf{S}^{(1)}_{clu},\mathbf{S}^{(2)}_{clu},\dots ,\mathbf{S}^{(n_{clu})}_{clu}$，其中第 $k$ 个聚类对应的中心点记为 $\mathbf{c}^{(k)}_{clu}$，同时其对应的半径为：
$$
r^{(k)}_{clu}= \max_{g_s^{i_k} \in \mathbf{S}^{(k)}_{clu}} \parallel  c^{(k)}_{clu} - g_s^{i_k} \parallel_{2}
$$

### B. Bidirectional Differential Evolution for Nonself Antigens
BDE 算法旨在从已知的抗原中创造可能的未知非自身抗原。BDE 算法的初始种群为所有已知的非自身抗原集合的子集，即 $\mathbf{G}_{ini} \in \mathbf{N}_{tr}$，与此同时，我们希望新创造的抗原离已知的自身抗原尽可能远，离已知的非自身抗原尽可能进。

**突变 Mutation**
BDE 过程包含 FDE（forward differential evolution）与 RDE（reverse differential evolution）两个过程，其中 FDE 的目标为创造离已知抗原更近的抗原，RDE 的目标为创造离自身抗原和已知非自身抗原更远的抗原。

对于第 $k$ 个簇，即 $\mathbf{S}^{(k)}_{clu}$，定义第 $t$ 代的 RDE 和 FDE 的种群为 $\mathbf{P}^{(k)}_{fde}(t)$ 和 $\mathbf{P}^{(k)}_{rde}(t)$。注意到第一代即（$t=1$）时，$\mathbf{P}^{(k)}_{fde}(t)=\mathbf{P}^{(k)}_{rde}(t)=\mathbf{G}_{ini}$。

对于前向过程 FDE 和反向过程 RDE，二者的突变策略是分开的，但形式类似，均为从父辈种群的随机组合，其中 RDE 的突变向量为：
$$
\begin{align*} \boldsymbol {v}^{\left ({k,l_{\text {r}}}\right)}_{\text {rde}}(t)=&\lambda _{1} \times \left [{ \boldsymbol {p}^{\left ({k,l_{\text {r}}}\right)}_{\text {rde}}(t) - \boldsymbol {g}^{\left ({i_{k}}\right)}_{\text {s}} }\right] \\&{} + \lambda _{2} \times \left [{ \boldsymbol {p}^{\left ({k,l^{\prime }_{\text {r}}}\right)}_{\text {rde}}(t) - \boldsymbol {p}^{\left ({k,l^{\prime \prime }_{\text {r}}}\right)}_{\text {rde}}(t) }\right] \end{align*}
$$
其中 $\boldsymbol {p}^{\left ({k,l^{\prime }_{\text {r}}}\right)}_{\text {rde}}(t), \; \; \boldsymbol {p}^{\left ({k,l^{\prime \prime }_{\text {r}}}\right)}_{\text {rde}}(t)$ 为对应第 $k$ 个簇的 RDE 的父代种群中的两个随机个体。将突变向量加上父代个体得到突变抗原：
$$
\begin{equation*} \boldsymbol {m}^{\left ({k,l_{\text {r}}}\right)}_{\text {rde}}(t) = \boldsymbol {p}^{\left ({k,l_{\text {r}}}\right)}_{\text {rde}}(t) + \boldsymbol {v}^{\left ({k,l_{\text {r}}}\right)}_{\text {rde}}(t). \end{equation*}
$$
对于 FDE 来说，其突变向量服从类似规则：仅在第一项上符号相反：
$$
\begin{align*} \boldsymbol {v}^{\left ({k,l_{\text {f}}}\right)}_{\text {fde}}(t)=&\lambda _{3} \times \left [{ \boldsymbol {g}^{\left ({i_{k}}\right)}_{\text {s}} - \boldsymbol {p}^{\left ({k,l_{\text {f}}}\right)}_{\text {fde}}(t) }\right] \\&{}+ \lambda _{4} \times \left [{ \boldsymbol {p}^{\left ({k,l^{\prime }_{\text {f}}}\right)}_{\text {fde}}(t) - \boldsymbol {p}^{\left ({k,l^{\prime \prime }_{\text {f}}}\right)}_{\text {fde}}(t) }\right] \end{align*}
$$
其对应的突变抗原为：
$$
\begin{equation*} \boldsymbol {m}^{\left ({k,l_{\text {f}}}\right)}_{\text {fde}}(t) = \boldsymbol {p}^{\left ({k,l_{\text {f}}}\right)}_{\text {fde}}(t) + \boldsymbol {v}^{\left ({k,l_{\text {f}}}\right)}_{\text {fde}}(t). \end{equation*}
$$

**交叉 Crossover**
注意在 mutation 过程中得到的突变抗原仍非我们最终用于测试的个体，最终测试个体 $u$ 由以下过程交叉过程生成：
$$
\begin{align*} u^{\left ({k,l_{\text {r}},d}\right)}_{\text {rde}}(t)=&\begin{cases} m^{\left ({k,l_{\text {r}},d}\right)}_{\text {rde}}(t),& {\mathrm {if}} ~\rho _{\text {rand}} \le \rho _{\text {cr}} ~\text {or} ~d = d_{\text {rand}} \\ p^{\left ({k,l_{\text {r}},d}\right)}_{\text {rde}}(t),& {\mathrm {otherwise}} \end{cases} \tag{11}\\ u^{\left ({k,l_{\text {f}},d}\right)}_{\text {fde}}(t)=&\begin{cases} m^{\left ({k,l_{\text {f}},d}\right)}_{\text {fde}}(t),& {\mathrm {if}} ~\rho _{\text {rand}} \le \rho _{\text {cr}} ~\text {or} ~d = d_{\text {rand}} \\ p^{\left ({k,l_{\text {f}},d}\right)}_{\text {fde}}(t),& {\mathrm {otherwise}} \end{cases} \tag{12}\end{align*}
$$
其中 $d$ 的含义为第 $d$ 个维度，即第 $d$ 个位置的坐标。$\rho_{\text{cr}}$ 为超参数交叉率，$\rho_{\text{rand}}$ 为随机概率，随机整数 $d_{\text{rand}}\in [1, n_d]$ 保证至少有一个维度是来自于突变抗原。

**选择 Selection**
在设定 RDE 的目标函数时，一个朴素的想法是希望新个体与簇的中心距离越大越好，即：
$$
\begin{equation*} \mathcal {F}^{(k)}_{\text {rde}}\left ({\boldsymbol {x}}\right) = \| \boldsymbol {x} - \boldsymbol {c}^{(k)}_{\text {clu}} \|_{2} \tag{13}\end{equation*}
$$
需注意到先前数据已经做过 Min-Max 归一化，其所有坐标都在 $[0,1]$ 之间，因此二者最远的距离实际上为 $\sqrt{n_d}$，由此真正的满足 RDE 条件的个体应为：
$$
\begin{equation*} \mathcal {F}^{(k)}_{\text {rde}}\left ({\boldsymbol {p}^{(k,l_{\text {r}})}_{\text {rde}}(t)}\right) < \mathcal {F}^{(k)}_{\text {rde}}\left ({\boldsymbol {u}^{(k,l_{\text {r}})}_{\text {rde}}(t)}\right) < \rho _{\text {rde}} \times \sqrt {n_{\text {d}}} \tag{14}\end{equation*}
$$
其中 $\rho_{\text{rde}}$ 为调整系数，取值在 $[1,2]$。

对于 FDE 类似，其目标函数为 RDE 目标函数的倒数：
$$
\begin{equation*} \mathcal {F}^{(k)}_{\text {fde}}(\boldsymbol {x}) = 1 \div \| \boldsymbol {x} - \boldsymbol {c}^{(k)}_{\text {clu}} \|_{2}. \tag{15}\end{equation*}
$$
考虑归一化后的坐标，满足条件的个体为：
$$
\begin{equation*} \mathcal {F}^{(k)}_{\text {fde}}\left ({\boldsymbol {p}^{(k,l_{\text {f}})}_{\text {fde}}(t)}\right) < \mathcal {F}^{(k)}_{\text {fde}}\left ({\boldsymbol {u}^{(k,l_{\text {f}})}_{\text {fde}}(t)}\right) < 1 \div \left ({\rho _{\text {fde}} \times r^{(k)}_{\text {clu}}}\right) \tag{16}\end{equation*}
$$
将经过 $t$ 期的进化后的个体集合记为：
$$
\begin{equation*} \mathbf {G}^{(k)}_{\text {bde}}(t) = \mathbf {G}^{(k)}_{\text {rde}}(t) \bigcup \mathbf {G}^{(k)}_{\text {fde}}(t). \tag{17}\end{equation*}
$$
当某个 $t$ 期的进化个体集合为空集时，终止对第 $k$ 个簇的进化过程，同时开启对第 $k+1$ 个簇的进化。