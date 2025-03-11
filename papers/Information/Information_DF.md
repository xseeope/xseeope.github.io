# A Information-theoretic Approach to Distribution Shifts

NeurIPS 2021

- Microsoft Research
- Unversity of Amsterdam

## Introduction
<!-- # 祝纪元 20250221 报告
重装系统后继续检查了可能的数据泄漏问题，andrew 的数据文档写的比较详细，未被验证的复权问题也自己检查确认过了。但是我们的 KAN 表现的主要在 shrinkage 这个数据集上，这个数据集怀疑点主要在 prc 这个价格字段的处理写的没有很清楚，但是我比较倾向于没有发生数据泄漏，我自己重新使用了 xgboost 和 mlp 在自己的框架下用相同的数据集做预测，表现都远弱于 KAN。这至少可以说明两件事，一、KAN 确实在这个任务上表现出了比较好的预测能力，二、数据有泄漏的可能比较小。

由于把 KAN 输入更改为面板数据和移植到 qlib 和中国数据上的工作依旧还是在 debug，所以暂时还没有实验结果可以分享。本次报告分享的是近期读到的关于 distribution shift 的工作，该工作主要从信息论理论视角分析分布漂移。在具体改善分布漂移方面，可以注意的是 Distribution shift 曾连续两年作为一个独立的专题出现在 NeurIPS 的 workshop 中（2022 年和 2023 年），已有一定数量的工作聚焦于此。

分布漂移往往与时序相关，例如，使用 1970 年的卫星图像训练的识别模型，其识别率在 2020 年代的卫星图像数据集上下降，这是由于训练集和测试集的分布已经发生了漂移。我相信金融市场也一样永远是动态的，即，如果把截面上的收益 $y$ 和特征 $\mathbb{x}$ 看作是随机变量，那他们的联合分布 $p(\mathbb{x}, y)$ 并不是时不变的，漂移无时不刻都在发生。 -->

## Problem Statement

定义 $x$ 和 $y$ 分别为特征和标签，其联合密度为 $p(x, y)$，且考虑的是预测问题。令 $t$ 为一个二元的随机变量，用于标记哪些数据被选择用于训练 $(t = 1)$，没有被用来训练的会被标记为 $(t = 0)$。将 $p(x, y | t = 1)$ 记为训练分布（Training distribution），而 $p(x, y | t = 0)$ 称为测试分布（Test distribution）。本文考虑 $t$ 的取值为一个为特征 $x$、目标 $y$、独立的噪声 $\mathbf{e}$ 以及其他影响数据收集过程的因素（例如地理位置、时间间隔、人口群体等）的函数。

令 $q(y | x)$ 表示一个可学习的模型，其被用于预测分布 $p(y | x)$。使用 Kullback-Leibler 散度来表达训练误差和测试误差：

训练误差：
$$
D_{KL}\left(p(y | x, t = 1) \parallel q(y | x)\right) := D_{KL}\left(p(y | x, t = 1) \parallel q(y | x)\right)
$$

测试误差：
$$
D_{KL}\left(p(y | x, t = 0) \parallel q(y | x)\right) := D_{KL}\left(p(y | x, t = 0) \parallel q(y | x)\right)
$$

自然，我们希望模型的测试误差尽量小。

而注意到 distribution drift 是来自于两方面的：
>[!TIP]
>- Covariate shift: 训练数据和测试数据的输入特征 $x$ 的分布发生了变化，但目标 $y$ 的生成机制（即在给定 $x$ 的情况下，$y$ 的概率分布）保持不变
>- Concept shift: 虽然输入特征的分布保持不变，但特征与目标之间的关系发生了变化。即使模型使用的特征相同，目标 $y$ 也可能在不同的时间或环境下有不同的生成机制

在本文中，利用 mutual information 对其 t 取值的影响进行解构：
$$
I(x, y; t) = I(x; t) + I(y; t | x)
$$

其中：
- **Distribution shift**：$I(x, y; t)$
- **Covariate shift**：$I(x; t)$
- **Concept shift**：$I(y; t | x)$

在面对一个存在分布漂移的任务时，要要想让样本内外的 KL 散度降到极小直觉上是不可能的，作者在文章也给出了其二者之和的下界为：
$$D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{x}}^{\mathrm{t}=1} \| q_{\mathbf{y} \mid \mathbf{x}}\right)+D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{x}}^{\mathrm{t}=0} \| q_{\mathbf{y} \mid \mathbf{x}}\right) \geq \frac{1}{1-\alpha} I(\mathbf{y} ; \mathrm{t} \mid \mathbf{x})$$

同时对 loss 进行拆分：
$$\begin{aligned} & D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{x}}^{\mathrm{t}=1}| | q_{\mathbf{y} \mid \mathbf{x}}\right) \leq \underbrace{I_{\mathrm{t}=1}(\mathbf{x} ; \mathbf{y} \mid \mathbf{z})}_{\text {Train information loss }}+\underbrace{D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{z}}^{\mathrm{t}=1}| | q_{\mathbf{y} \mid \mathbf{z}}\right)}_{\text {Latent train error }} \\ \;\\& 
D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{x}}^{\mathrm{t}=0} \| q_{\mathbf{y} \mid \mathbf{x}}\right) \leq \underbrace{I_{\mathrm{t}=0}(\mathbf{x} ; \mathbf{y} \mid \mathbf{z})}_{\text {Test information loss }}+\underbrace{D_{\mathrm{KL}}\left(p_{\mathbf{y} \mid \mathbf{z}}^{\mathrm{t}=0}| | q_{\mathbf{y} \mid \mathbf{z}}\right)}_{\text {Latent test error }} .\end{aligned}$$

利用此拆解，作者获得了分析不同 criterion 对 covariat shift 和 concept shift 造成的 loss 的影响的工具。

其理论和实践上验证了包括 *information bottleneck* 在内的五种 criterion 对我们关心的 concept shift 造成的 loss 有效。