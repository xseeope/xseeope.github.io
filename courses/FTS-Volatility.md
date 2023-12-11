# FTS-Volatility

## Intro

### What is it?

In financial field, the word volatility often denotes the ==conditional== standard deviation of the asset returns

### Characteristics of financial volatility 

- Cannot be observed directly

- Others,,,,

### Basic idea of modeling the volatility

- Shocks of asset returns are NOT serially correlated, but dependent
- The serial dependence is nonlinear
- Volatility models are built to capture such nonlinear dependence in the return series

Volatility is assumed to be a function of available information.
$$
\sigma_t^2= Var(r_t|F_{t-1})=Var(a_t|F_{t-1})
$$
Fixed function of the available information: ARCH, GARCH, ICHARCH, etc.

Stochastic function of the available information: Stochastic volatility models (SV), etc.

## ARCH

$$
a_t=\sigma_t\epsilon_t, \qquad \sigma_t^2=\alpha_0+\alpha_1a_{t-1}^2+\cdots+\alpha_ma_{t-m}^2 
$$

Note that,

- $\alpha_0 >0,\quad\alpha_i \geq 0$
- Mean and variance of $\epsilon_t$ is 0 and 1, and the distribution could be, 
  - Normal distribution
  - standard t
  - standard generalized error distribution

### Fourth moment and heavy tail

The 4th moment of ARCH(1)'s $a_t$ is :
$$
m_4=\frac{3\alpha_0^2(1+\alpha_1)}{(1-\alpha_1)(1-3\alpha_1^2)}
$$
From the 4th moment, we can proof that the Kurosis is greater than 3, which means a heavier tail than the normal distribusiton.

### Steps of building an ARCH model

- Testing of there is an ARCH effect, using $H_0$
- Order estimation, using PACF
- Estimation: conditional MLE
- Model checking: Q-stat, Kurosis, etc.

### Weakness of ARCH

- Symmetric
- Restrictive
- No explanation
- Likely to overestimate volatility 
- Often requires many parameters to adequately describe the volatility 

## GARCH

Generalized ARCH

### What is it?

For a GARCH(m,s),
$$
a_t=\sigma_t\epsilon_t, \\
\sigma_t^2=\alpha_0+\sum\limits_{i=1}^m\alpha_ia_{t-i}^2+\sum\limits_{j=1}^s\beta_j\sigma_{t-j}^2\\
$$
Note that

- $\alpha_0 >0,\quad\alpha_i \geq 0, \quad \beta_j \geq 0$
- $\sum(\alpha_i+\beta_i)<1$
- Zero mean and unit variance assumption
- m as the ARCH order, s as the GARCH order
- Non-negative constraints on (G)ARCH coefficients