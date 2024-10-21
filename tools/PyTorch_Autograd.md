# PyTorch Autograd Mechanics
- PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.

## How autograd encodes the history
> Autograd is a reverse automatic differentiation system.

Conceptually，在对数据进行操作时，autograd 会将所有的 operation 记录为一个有向无环图（directed acyclic graph），其中叶为输入张量，根为输出张量。从根到叶，可以自动通过链式法则计算梯度。

Internally，autograd 把操作过程表示为一个 `Function` 对象的图。当在执行前向过程时，autograd 会同步构建用于计算梯度的函数。在前向过程执行完毕后，在后向过程中会完成梯度的计算。当调用 `.backward()` 时，PyTorch 会通过 `grad_fn` 对象来计算每个 `Tensor` 的梯度，并将它们存储在对应的 `.grad` 属性中。

需要注意的是，该记录 operation 的 DAG（有向无环图）会在每次的迭代中都重新生成。该特性实际上允许在不同的迭代中使用不同的 Python control flow statements 且不影响梯度计算，what you run is what you differentiate。

## Gradients for non-differentiable functions
在使用 Automatic Differentiation 计算梯度时，其一个必要条件为 elementary function 必须可导。然而在实践中，许多函数并不满足这个条件，如 `ReLU` 和 `sqrt` 在 `0` 处。为此，PyTorch 定义了一系列规则使得其影响降到最小，并尽量返回梯度计算值或 `NaN`，但当所谓的 “function” 并不是一个确定映射时（也就是说这并不是一个数学定义上的函数时），将会导致报错。

## Locally disabling gradient computation


## References
- https://pytorch.org/docs/stable/notes/autograd.html

