# Deep Learning in Asset Pricing

**Journal:**

Management Science (accepted in 2022)

**Authors:**

- Luyang Chen:

  Stanford University

- Markus Pelger:

  Stanford University

- Jason Zhu:

  Stanford University

## Abstract

We use deep neural network to estimate an asset pricing model for individual stock returns that takes advantage of the vast amount of conditioning information, keeps a fully flexible form, and accounts for time variation. The key innovations are to use the fundamental no-arbitrage condition as criterion function to construct the most informative test assets with an adversial approach and to extract the states of the economy from many macroeconomic time series. Our asset pricing model outperforms out-of-sample all benchmark approach in terms of Sharpe ratio, explained variation, and pricing errors and identifies the key factors that drive asset prices.

## Introduction

如何解释不同资产平均回报之间的差异是资产定价的基本问题。无套利理论提供了一个清晰的答案：期望收益存在差异的原因在于不同资产对 SDF 也就是定价核的暴露不同。过去 40 年的实证资产定价工作一直在探寻如何估计可以解释所有资产回报的 SDF。在统一的框架下估计 SDF 存在如下四个主要挑战：一、SDF 可以通过**所有**可用信息构造，这意味着 SDF 是关于海量自变量的函数；二、SDF 的函数形式未知并且很可能复杂度较高；三、SDF 很可能存在复杂动态结构，由于经济状态和资产本身属性的变化，具体资产的风险暴露很大可能是时变的；四、个股的风险溢价的低信噪比，使得估计能解释所有股票的 SDF 变得更加棘手。

机器学习技术善于解决高维与高复杂性问题，但是本文讨论的问题还具有低信噪比的特征，现有的机器学习方法在低信噪比环境下具有较大的局限性。
                                                   
本文通过大量的宏观经济与公司信息，使用深度神经网络构建针对美国股票市场的非线性资产定价模型。本文核心创新点在于将无套利条件应用在神经网络算法中。

作者在本文中试图回答资产定价领域中以下三个问题：一、基于给定的信息集合，SDF 的函数形式如何？Factor zoo 表明存在远超 FF5 数量的可作为定价信息的特征，流行的 FF5 模型不是正确答案；二、什么是正确的测试资产？传统上，评估资产定价模型常基于一些预先指定的测试资产如 Fama-French 双重排序组合。然而，一个可以很好地解释这 25 个资产的模型可以不需要捕捉其他特征信息，而 factor zoo 的存在已经说明了其他特征信息的重要性。本文通过数据挖掘方法去构造最难被解释的 the most informative test assets；三、现在的经济状态的确定。本文通过大量的宏观经济的动态时间序列信息来提取最与资产定价相关的状态过程。

本文过 MLP 作为 SDF 函数的 representation；使用 LSTM 捕捉 SDF 与经济状态之间的时变关系；使用 GAN 构造测试资产；使用无套利条件作为三个网络之间的联系和正则化。