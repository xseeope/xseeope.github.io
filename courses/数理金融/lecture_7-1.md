# General probability theory, asset price models and B-S formulas

## 1. Probability Space

$\Omega$ 是给定的集合，其 $\sigma$ 代数 $\mathcal{F}$ 是由 $\Omega$ 的子集组成，$\sigma$-algebra $\mathcal{F}$ 具有如下性质：

* $\emptyset \in \mathcal{F}$
* $F\in\mathcal{F}\Rightarrow F^C\in\mathcal{F}, F^C=\Omega\backslash F (补集)$
* $A_1,\ A_2,\ \cdots \in \mathcal{F} \implies A \equiv \cup_{i=1}^{\infty} A_i \in \mathcal{F}$

$(\Omega,\ \mathcal{F})$ 称作 **可测空间 (measurable space)**

基于可测空间 $(\Omega,\ \mathcal{F})$ 上的概率测度 $\mathbb{P}$ 是一个函数：$\mathcal{F} \to [0,\ 1] \ \ (映射到累积分布函数)$：

* $\mathbb{P}(\emptyset)=0, \mathbb{P}(\Omega)=1$
* If $A_1,\ A_2,\ \cdots \in \mathcal{F}$ and $A_i \cap A_j = \emptyset \ (i\neq j)$, then $\mathbb{P}\left( \cup_{i=1}^{\infty} A_i \right) = \sum\limits_{i=1}^{\infty} \mathbb{P}(A_i) $

$(\Omega,\ \mathcal{F},\ \mathbb{P})$ 称作 **概率空间 (probability space)**

## 2. Random Variable and Distribution

## 3. Expectations

$X$ 是概率空间 $(\Omega,\ \mathcal{F},\ \mathbb{P})$ 上的一个随机变量：

$$
\mathrm{E}(X) = \int_\Omega X(\omega)\ \mathrm{d}\mathbb{P}(\omega) \tag{1}
$$

$$
\mathrm{E}(\left\vert X \right\vert ) = \int_\Omega \left\vert X(\omega) \right\vert\ \mathrm{d}\mathbb{P}(\omega) < \infty \tag{2}
$$

(2) 式成立时，(1) 式成立；或 $X \geq 0 \quad a.s.$

这一设定的目的是为了保证 $\mathrm{E}(X)$ 是存在的

**Jensen's Inequality**

$\varphi$ 是一个实值的凹函数，若 $\mathrm{E}(\left\vert X \right\vert ) < \infty, \ \mathrm{E}(\varphi(X)) < \infty$，则：

$\varphi(\mathrm{E}(X)) \leqslant \mathrm{E}(\varphi(X))$

## 4. Change of Measure (测度变换)

假设现实世界的概率测度为 $\mathbb{P}$，存在与其对应的另一概率测度 $\widetilde{\mathbb{P}}$，定义随机变量 $Z, \ Z_i = \dfrac{\widetilde{\mathbb{P}}_i}{\mathbb{P}_i}$，则：

$
\begin{aligned}
    \mathbb{E}Z &= \mathbb{P}_1\dfrac{\widetilde{\mathbb{P}}_1}{\mathbb{P}_1} + \mathbb{P}_2\dfrac{\widetilde{\mathbb{P}}_2}{\mathbb{P}_2} + \cdots + \mathbb{P}_n\dfrac{\widetilde{\mathbb{P}}_n}{\mathbb{P}_n}\\
    \\
    &=\widetilde{\mathbb{P}}_1+\widetilde{\mathbb{P}}_2+\cdots+\widetilde{\mathbb{P}}_n\\
    \\
    &=1
\end{aligned}
$

若随机变量 $Z$ 满足 $\mathbb{E}Z=1, Z \geq 0$，对属于 $\mathcal{F}$ 的事件 $A$，定义：

$\tilde{\mathbb{P}}\left(A\right)=\int_{A}Z\left(\omega\right)d{\mathbb{P}}\left(\omega\right)$

于是 $\widetilde{\mathbb{P}}$ 是新的概率测度，且满足:

$$
\widetilde{\mathrm{E}}(X) = \mathrm{E}(XZ) \tag{3}
$$

若 $Z > 0$，则 $\mathrm{E}(Y) = \widetilde{\mathrm{E}}\left(\frac{Y}{Z}\right)$

>[!TIP|label:等价概率测度]
>可测空间 $(\Omega,\ \mathcal{F})$ 上的两个概率测度 $\mathbb{P},\widetilde{\mathbb{P}}$ 等价 (equivalent) 的条件：$\\$
>
>* ${\mathbb{P}}_i$ 和 $\widetilde{\mathbb{P}}_i$ 不为0时，它们可以不相等；$\\$
>* 但其中一个为0时，另一个必须也为0 (${\mathbb{P}}_i=0 \Longleftrightarrow \widetilde{\mathbb{P}}_i = 0$)

若 $\mathbb{P},\widetilde{\mathbb{P}}$ 等价，$Z$ 被称作 $\widetilde{\mathbb{P}}$ 关于 $\mathbb{P}$ 的 Radon-Nikodym derivative

$Z=\dfrac{d \widetilde{\mathbb{P}}}{d \mathbb{P}}$

<details>
<summary><font color=orange>例1：</font></summary>

$\Omega=\{H,T\},\ \mathbb P(H)=\mathbb P(T)=0.5;\ \mathbb Q(H)=0.2,\mathbb Q(T)=0.8$

the Radon-Nikodym derivative of $\mathbb Q$ with respect to $\mathbb P$ is:

$\qquad f(H)=\dfrac{0.2}{0.5} = 0.4$

$\qquad f(T)=\dfrac{0.8}{0.5} = 1.6$
</details>

<details>
<summary><font color=orange>例2：</font></summary>

$\Omega=\left[0,1\right], \ \mathbb{P}$ is the uniform (i.e., Lebesgue) measure

$Z(\omega)=2\omega$

则，$\tilde{\mathbb{P}}[a,b]=\int_a^b2\omega d\omega=b^2-a^2,0<a<b<1$
</details>

<details>
<summary><font color=orange>例3：</font></summary>

设 $X$ 是概率空间 $(\Omega,\ \mathcal{F},\ \mathbb{P})$ 上的标准正态随机变量，$\theta >0$，寻找与 $\mathbb{P}$ 等价的概率测度 $\widetilde{\mathbb{P}}$，使得 $X+\theta$ 是新的概率空间 $(\Omega,\ \mathcal{F},\ \widetilde{\mathbb{P}})$ 上的标准正态随机变量

设 $Z$ 是 $\widetilde{\mathbb{P}}$ 关于 $\mathbb{P}$ 的 Radon-Nikodym derivative，于是：

$\qquad \widetilde{\mathrm{E}}(X+\theta) = \mathrm{E}(XZ)$

因为 $X+\theta$ 是 $(\Omega,\ \mathcal{F},\ \widetilde{\mathbb{P}})$ 上的标准正态随机变量，于是：

$\qquad \widetilde{\mathrm{E}}(X+\theta) = \int_\Omega \frac{1}{\sqrt{2\pi}} e^{-\frac{(X(\omega)+\theta)^{2}}{2}}\ \mathrm{d}\omega$

$\qquad \mathrm{E}(XZ) = \int_\Omega \frac{1}{\sqrt{2\pi}} e^{-\frac{(X(\omega))^{2}}{2}}\cdot Z(\omega)\ \mathrm{d}\omega$

联立求解 $Z(\omega)$：

$\qquad Z(\omega) = exp\big(-\theta X(\omega) - \frac{1}{2}\theta^{2}\big),\quad \forall \omega \in \Omega$
</details>