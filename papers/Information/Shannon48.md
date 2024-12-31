# A Mathematical Theory of Communication
- C.E. SHANNON
- The Bell System Technical Journal

## Introduction
**Points:**

- 通信的基本问题: 在某个点完全或近似重构在另一个点选择的消息（message）。
- 【真实消息】是【可能消息】集合中的一个元素。
- 系统必须被设计为可以处理所有【可能消息】。
- 当在可能消息的集合中选择一个消息，就产生了【信息】，所有选择的可能性是相等的。
- 如果消息集合中的元素个数是 finite 的，那么这个个数或任何这个个数的单调函数都可以是信息的度量（measure of the information）。
- 使用对数度量有以下好处：
  1. 贴近实践
  2. 符合直觉
  3. 数学上的处理更加容易

## General Communication System:
![Fig1](Shannon48Fig1.png)


*Information source* 产生消息（message）。消息的实例可以有：字母序列；关于时间的函数 $f(t)$；关于时间与其他变量的函数；多个关于多个变量的函数。

*Transmitter* 将消息（message）加工为信号（signal），使得其更适于在信道（channel）中传输。

*Channel* 用来传输信号的介质，如电线、光缆、射频带。

*Recevier* 从信号中重构消息。

*Destination* 这个消息所指向（intended）的人或实体