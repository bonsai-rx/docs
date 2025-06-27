---
uid: reactive-average
title: Average
---

![Marble diagram](~/images/reactive-average.svg)

The `Average` operator collects all the values from the source sequence and emits a single floating-point number representing their arithmetic mean. The single result value is emitted only when the source sequence terminates successfully.

### Examples

Use `Average` to report the mean value at the end of the sequence.

:::workflow
![Average Example](../workflows/reactive-average-example.bonsai)
:::

#### Signal Smoothing

Use `Average` to smooth a noisy signal by grouping elements with [`WindowCount`](xref:Bonsai.Reactive.WindowCount), then applying `Average` inside a [`SelectMany`](xref:Bonsai.Reactive.SelectMany).

:::workflow
![Average Application Downsample](../workflows/reactive-average-application-downsample.bonsai)
:::

> [!NOTE]
> This operation is equivalent to [downsampling](https://en.wikipedia.org/wiki/Downsampling_(signal_processing)) and reduces the number of elements in the sequence. To implement a [moving average](https://en.wikipedia.org/wiki/Moving_average) that preserves the number of elements, you can adjust the `Skip` property in [`WindowCount`](xref:Bonsai.Reactive.WindowCount) to create sliding windows.

> [!NOTE]
> This example requires the `Bonsai.Design.Visualizers` package to be installed for time series visualization.