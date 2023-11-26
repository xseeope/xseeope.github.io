# Predicting Returns with Text Data

**Journal:**

NEBR working paper(Posted: 03 Sep 2019 Last Revised: 21 Jul 2023)

**Authors:**

- Zheng Tracy Ke:

  Harvard University

- Bryan T. Kelly:

  Yale SOM; AQR Capital Management, LLC; National Bureau of Economic Research (NBER)

- Dacheng Xiu:

  University of Chicago - Booth School of Business

## Abstract

We introduce a new text-mining methodology that extracts sentiment information from news articles to predict asset returns. Unlike more common sentiment scores used for stock return prediction (e.g., those sold by commercial vendors or built with dictionary-based methods), our supervised learning framework constructs a sentiment score that is specifically adapted to the problem of return prediction. Our method proceeds in three steps: 1) isolating a list of sentiment terms via predictive screening, 2) assigning sentiment weights to these words via topic modeling, and 3) aggregating terms into an article-level sentiment score via penalized likelihood. We derive theoretical guarantees on the accuracy of estimates from our model with minimal assumptions. In our empirical analysis, we text-mine one of the most actively monitored streams of news articles in the financial system|the Dow Jones Newswires|and show that our supervised sentiment model excels at extracting return-predictive signals in this context.

作者引入了一种新的文本挖掘方法，该方法从新闻文章中提取情感信息以预测资产回报。与用于股票回报预测的更常见的情感分数不同（例如，那些由商业供应商出售或使用基于词典的方法构建的情感分数），作者的监督学习框架构建了一个专门适用于回报预测问题的情感分数。方法分为三个步骤：1）通过predictive screening分离出一个情感词的表，2）通过topic modeling为这些词分配sentiment weights，3）通过penalized likelihood将词语聚合到文章级别的sentiment score。作者从模型中得出对估计准确性的理论保证，同时做出最小的假设。在实证分析中，作者使用道琼斯新闻社的文本数据，结果显示作者提出的有监督的sentiment model在提取回报预测信号方面表现出色。

## Introduction

> While the natural language processing and machine learning literature is growing increasingly sophisticated in its ability to model the subtle and complex nature of verbal communication, usage of textual analysis in empirical finance is in its infancy.

在机器学习与自然语言模型大行其道的当下，作者形容文本分析在金融实证研究的应用还是个婴儿。

Document sentiment scores在之前的研究中被用作一个辅助模型，用于分析例如金融市场中的信息传递现象的研究（Tetlock, 2014）。其他在这个领域比较有影响力的论文如Tetlock在2007年的工作和Loughran and McDonald在2011年的工作虽然取得了一些成果，但他们都还是用的过去的语料库去分析。

> In contrast with this literature, we develop a machine learning method to build context-specific sentiment scores. We construct and evaluate the performance of trading strategies that exploit our sentiment estimates, and find large economic gains, particularly out-of-sample. Finally, our analysis of the speed of news assimilation in asset prices contributes to the literature on information transmission in finance, as surveyed by Tetlo ck (2014).

这篇文章的主要贡献有：

- 使用机器学习方法构建特定上下文的sentiment scores构建投资组合，并且样本外收益效果拔群
- 分析了资产价格对新闻的吸收速度

模型优点有：

- 可解释性，作者提出的有监督模型是*”entirely white box“*
- 计算复杂度低，百万数量级的文档在笔记本长处理完只需几分钟
- 可自定义性，该模型允许其他使用者根据自己使用的文本数据进行调试，让研究者不再依赖第三方库

## Methodology

### Notation

考虑$n$ news articles 和 a dictionary of $m$ words。组成一个$n\times m$的矩阵$D = [d_1,\dots,d_n]'$。其中$d_{i,j}$表示第$i$篇文章中词语$j$出现的次数。文中有时还会用到 $D$ 的列的子集，这些列的索引的集合被定义为 $S$ 。分别定义这些子矩阵与子矩阵中第 $i$ 个列向量为$D._{,[S]}$和$d_{i,[S]}$ 。

作者使用的新闻数据中自带公司的tag，在这篇文章中，作者也只研究了含有该公司tag的新闻对该公司收益 $y_i$ 的影响。

同时作者假设所有的文章都具有一个情感分数 sentiment score $p_i \in [0,1]$ 。当 $p_i = 1$ 时认为是最积极，当$p_i=0$ 时认为其最消极。同时作者假设 $p_i$ 是文章对股票回报的充分统计量，换句话说，在给定$p_i$的条件下，$d_i$ 与 $y_i$ 是独立的。

### Model Setup

$sgn(x)$ 表示的是符号函数，当 $x>0$ 时 $sng(x)=1$ 其他情况时等于0，下面这个表达式实际上说的是 sentiment score 越高就越有可能实现一个正收益。
$$
\mathbb{P}(sgn(y_i)=1)=g(p_i), for\;a\;monotone\;increasing\;function\;g(\cdot)
$$
注意到这个表达式的假设是很弱的，我们并不需要知道 $y_i$ 的具体分布或者是 $g(\cdot)$ 的具体形式。

同时假设词典 $dictionary$ 有如下的分割：
$$
\{1,2,\dots,m\}=S\,\cup\, N
$$
其中 $S$ 是sentiment-charged words的索引的集合，维度为$|S|$，$N$ 则是情感中性词sentiment-neutral words的索引的集合,维度为 $m-|S|$。$\{1,2,\dots,m\}$ 为所有在词典中的词的索引的集合。

作者假设 $d_{i,[S]}$ 与 $d_{i,[N]}$ 之间互相独立，且认为中性词无关紧要而且维度过高，因此本文不对中性词进行建模。

作者假设还包括 $d_{i,[S]}$ 服从混合多项式分布mixture multinomial distribution：
$$
d_{i,[S]}\sim Multinomial(s_i,\;p_iO_++(1-p_i)O_-)
$$
其中 $s_i$ 表示在文章 $i$ 中情感词sentiment-charged words的个数， $s_i$ 决定了该多项式分布的scale。$O_+$ 是单词的概率分布，其形式为长度为 $|S|$ ，$l^1$ 范数为1，并且所有元素非负的向量。$O_+$ 描述了在一个极端积极（$p_i=1$）时词语的期望频率。$O_-$ 同理。$O_+$ 被称为positive sentiment topic，$O_-$ 被称为negative sentiment topic。

一般情况下 $0<p_i<1$ ，此时单词的频率为positive和negative topic的convex combination。举例：词语“up”在一个极端积极的新闻中出现的频率期望为0.8，在一个极端消极的新闻中出现的频率期望为0.1，则其在一篇sentiment score为0.6的文章中出现的期望频率为 $0.6\times0.8+(1-0.6)\times0.1=0.52$ 。

![Figure1](/figures/Figure1.png)

这个模型的关键在于估计 $O_+$，$O_-$ ，$p_i$。具体来说，SESTM有三个步骤：

- 分离出sentiment-charged words
- 估计 $O_+$，$O_-$ 
- 预测一片新文章的sentiment score $p_i$

### Screening for Sentiment-Charged Words

Sentiment-neutral words很坏，因为它们的维度很高且在文中的占比很大，因此需要剔除它们，分离出sentiment-charged words。

作者使用了一个有监督的方法去找出sentiment-charged words。Intuitively，就是如果一个词与正收益经常一起出现，那么可以认为这个词携带了一定的积极情绪。这个筛选机制的第一步是计算频率：
$$
f_j=\frac
{\# articles\; \;including\; \;word\;\; j\;\;AND\;\;having\;\;sgn(y)=1}
{\# articles\;\;including\;\;word\;\;j}
$$
这种方法在统计学中被称作marginal screening，与其他更复杂的方法相比该方法在信噪比低的情况下有理论优势。

第二步设置三个阈值：$\alpha_+,\alpha_-,\kappa$。如果$f_j>1/2+\alpha_+$，那么认为词 $j$ 为积极词postive sentiment words，如果$f_j<1/2-\alpha_-$则认为其为消极词negative sentiment words。$\kappa$ 则是对 $f_j$ 的分母起到了限制作用。

在给定$(\alpha_+,\alpha_-,\kappa)$的情况下，可以构造出list of sentiment-charged words，也就是 $S$：
$$
\hat{S}=\{j:f_j\geq1/2+\alpha_+,or\;f_j\leq1/2+\alpha_-\}\cap\{j:k_j\geq\kappa\}
$$
上面过程可以总结为Algorithm 1：

![算法1](figures/算法1.png)

### Learning Sentiment Topics

把两个topic vector合并为一个矩阵 $ O=[O_+,O_-]$ 。定义 $vactor \;of\;frequency,F$ 与 $ vector\;of\;tone, T$：
$$
F=\frac{1}{2}(O_++O_-),\qquad T=\frac{1}{2}(O_+-O_-)
$$
如果一个词语在 $F$ 的值比较大，说明其在总体水平上出现频率很高；如果其 $T$ 值较高，则说明其情感色彩更为积极。设定 $\tilde{d_{i,[S]}} = d_{i,[S]}/s_i$ ，为词频率向量，根据之前设定的模型则有：
$$
\mathbb{E}\tilde{d_{i,[S]}}=\mathbb{E}\frac{d_{i,[S]}}{s_i}=p_iO_++(1-p_i)O_-
$$
或者写成矩阵形式：
$$
\mathbb{E}\tilde{D'}=OW,\quad 
W=\begin{bmatrix} p_1 & \cdots & p_n \\ (1-p_1) & \cdots &(1-p_n)\end{bmatrix},\quad
and\quad \tilde{D'}=[\tilde{d_1},\dots,\tilde{dn}]'
$$
别忘了我们在这一部分是要估计 $O$ ，那么要怎么估计呢，作者使用了一个简单的方法，就是通过 $\tilde{D}$ 对 $W$ 的回归来估计 $O$。那么问题又来了，$\tilde{D}$ 和 $W$ 是从哪来的呢？$\tilde{D}$ 实际上就是用算法1中得到的 $\hat{S}$ 算出来的。而对于 $W$ 作者则使用标准化的收益排名作为训练样本的sentiment score：
$$
\hat{p_i}=\frac{rank\;of\;y_i\;in\; \{y_l \}_{l=1}^n}{n}
$$
对于 $O$ 的估计总结为algorithm 2：

![算法2](/figures/算法2.png)

作者在附录中指出，该方法对于 $F$ 的估计是一致的，但是对于 $T$ 的估计存在偏误，这个偏误与true sentiment和estimated sentiment之间的correlation有关，其形式为：
$$
\rho = \frac{12}{n}\sum_{i=1}^n(p_i-\frac{1}{2})(\hat{p_i}-\frac{1}{2})
$$
Theorem C.3还指出 $\hat{T}$ 会收敛到 $\rho T$ 。因此对 $\hat{\rho}$ 的估计越准确，偏误就越低。但是这种的偏误对实际应用没有影响，因为在实践中，我们感兴趣的是词之间的相对情绪relative sentiment，而不是绝对情绪absolute sentiment。在我们只关注relative sentiment的情形下，$\rho$ 的影响会被完全消除。

考虑 $n$ 篇文章，词汇表size为 $|S|$，也就是说 $S$ 中单词的数量，以及平均文章长度 $\bar{s}$ ，对于 $F, S$ 的估计误差的收敛速率为$\sqrt{|S|/(n\bar{s})}$。在实证中，一个sentiment dictionary大约包含100到200个单词，然而它们在一篇文章中的总数通常不超过20。考虑到这样的收敛速率的形式，作者主要关注的对象为“短文章”也就是 $\bar{s}/|S|$ 的值比较小的情况。作者宣称其使用有监督学习主要也是考虑到收敛速度。

### Scoring New Articlas

通过前面两步，我们已经得到了 $\hat{S},\hat{O}$，现在我们要用它们来估计样本外的文章 $i$ 的sentiment score了。回忆一下之前的模型：
$$
d_{i,[S]}\sim Multinomial(s_i,\;p_iO_++(1-p_i)O_-)
$$
其中 $d_i$是这篇文章的count vector，$s_i$ 是这篇文章的所有sentiment-charged words。我们可以用极大似然估计来估计 $p_i$。

作者在似然函数中增加了一个惩罚项 $\lambda log(p_i(1-p_i))$，惩罚的作用是帮助应对有限的观测数量和与股票回报预测本身的低信噪比。且大多数的文章其实是中性的neutral- sentiment，而加入的惩罚项会导致估计量朝着1/2收缩，使得模型更符合现实情况。且作者在实际研究中也发现不加惩罚项会使得 $\hat{p_i}$ 收敛至 $\frac{1}{2}+\frac{1}{\rho}(p_i-\frac{1}{2})$， 加入了惩罚项可以deflate偏误。

Algorithm 3：

![算法3](/figures/算法3.png)

## Empirical Analysis

### Data and Pre-processing

Text data:

- 来源：*Dow Jones Newswires Machine Text Feed and Archive* database
- 时间：January 1, 1989 to July 31, 2017
- 数量：22,471,222
- 去除包含多个stock tag的新闻（大约62.5%）

![Figure3](/figures/Figure3.png)

![table1](/figures/table1.png)

由于事先不知道新闻稿中的潜在新信息何时被纳入价格中。如果价格调整缓慢，那么将文章与同时期回报以及未来回报对齐是有道理的。新闻稿对于市场参与者来说是一个非常显眼的信息来源，因此价格反应的任何延迟可能是短暂的。同时考虑到，新闻稿也可能是对已经披露的信息的重新表述，这种情况下，将新闻与先前的回报match可能更为合适。作者最终选择将t时刻的文本数据与t-1到t+1时刻的收益数据做match。但是这个match只用于训练参数，但在实操上，是把这个参数用于预测未来的收益。

作者按照自然语言处理文献中的常见步骤来清理和结构化新闻文章。第一步是归一化，包括1）将文章中的所有单词更改为小写字母；2）扩展缩写，如将“haven't”扩展为“have not”；以及3）删除数字、标点符号、特殊符号和非英语单词。第二步是词干提取和词形还原，将一个词的不同形式分组在一起，以分析它们作为一个根词，例如，“disappointment”变为“disappoint”，“likes”变为“like”等。第三步则是将每篇文章分割成一个一个单词。第四步删除常见的停用词，如“and”、“the”、“is”和“are”。

### Daily Predictions

![table2](/figures/table2.png)

![Figure5](/figures/Figure5.png)

作者的交易策略比较直接：每天买入情感得分最高的50只股票，并卖空情感得分最低的50只股票。策略的多空头构建考虑了等权重和市值加权两种方案。

等权多空组合年化夏普比率为4.29，而市值加权情况下为1.33。这表明，sentiment对未来小盘股回报的预测能力更强。同时交易中的多头表现优于空头，夏普比率为2.12对比1.21（等权多空）。同时以Fama-French作为benchmark时，几乎所有的收益来源都来自于 $\alpha$ 。

### Speed of Information Assimilation

回忆一下，作者的模型是用t-1期到t+1期的收益与t期的新闻数据训练的并分析了t+1期收益与t期的新闻数据之间的关系，但除此之外，作者还分析了新闻的传递速度。

![Figure7](/figures/Figure7.png)

上图图七中，红色虚线为利用0时刻的新闻构造0时刻的投资组合的对数收益，红色虚线为用0时刻的新闻构造-1时刻的投资组合的对数收益（注意这两种构造方法在现实中是无法实现的，但作者认为可以新闻与不同期的realized return之间的关系）。

Day-1策略实际上量化了构造的sentiment score对旧新闻的捕捉程度，其年化Sharpe为5.88，作者同时认为Day 0策略反应的是情感评分多大程度上捕捉到了之前未被纳入价格的新信息，其年化Sharpe高达10.78。Day-1策略则量化了sentiment score中的信息在多大程度上被延迟注入价格中，其年化Sharpe为4.29。

那么除了Day-1 0 1策略之外，那么作者顺着这个思路去构造了不同delay的portfolio，并比较他们的收益（Figure8）。

![Figure8](/figures/Figure8.png)