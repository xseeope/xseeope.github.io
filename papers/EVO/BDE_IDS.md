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
