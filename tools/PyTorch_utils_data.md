# Dataloader
- `torch.utils.data.Dataloader` 类为数据集上的 Python 迭代器提供了一个表示

构造 Dataloader 参数如下：

```Python
DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, *, prefetch_factor=2,
           persistent_workers=False)
```
## Dataset types
对于 `Dataloader` 来说，其最重要的参数为 `dataset` 。PyTorch支持两种类型的数据集

- map-style datasets
- iterable datasets

### Map-style datasets
该类型数据集可以通过 `dataset[idx]` 访问第 `idx` 个图像和其对应的 label。

### Iterable-style datasets
该类型数据集为 `IterableDataset` 的子类的一个实例。该类型通常很适用于随机读取成本高昂的场景，该类型数据集的 batch size 取决于提取的数据。

> For example, such a dataset, when called `iter(dataset)`, could return a stream of data reading from a database, a remote server, or even logs generated in real time.

## References
- https://pytorch.org/docs/stable/data.html