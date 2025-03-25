---
uid: reactive-average
title: Average
---

![Marble diagram](~/images/reactive-average.svg)

The `Average` operator collects all the values from the source sequence and emits a single floating-point number representing their arithmetic mean. The single result value is emitted only when the source sequence terminates successfully.

### Examples
Use `Average` to report the mean value at the end of the sequence.

:::workflow
![Mean](../workflows/reactive-average-example-mean.bonsai)
:::

> [!NOTE]
> The [`Delay`](xref:Bonsai.Reactive.Delay) operator is used in this example only to keep the workflow open long enough to visualize the result. Since only a single value is emitted, use an [`ObjectTextVisualizer`](xref:Bonsai.Design.ObjectTextVisualizer) to visualize it.

Use `Average` to apply a smoothing operation to the sequence by grouping elements with [`WindowCount`](xref:Bonsai.Reactive.WindowCount) and placing `Average` inside a [`SelectMany`](xref:Bonsai.Reactive.SelectMany).

:::workflow
![Downsample](../workflows/reactive-average-example-downsample.bonsai)
:::

> [!NOTE]
> This operation is equivalent to downsampling and reduces the number of elements in the sequence. To implement a moving average that preserves the number of elements, you can adjust the `Skip` property in [`WindowCount`](xref:Bonsai.Reactive.WindowCount) to create sliding windows.