---
uid: reactive-average
title: Average
---

![Marble diagram](~/images/reactive-average.svg)

The `Average` operator collects all the values from the source sequence and emits a single floating-point number representing their arithmetic mean. The single result value is emitted only when the source sequence terminates successfully.

### Examples
Use `Average` to report the mean value (such as the interval between key presses) at the end of the sequence.

:::workflow
![Mean](../workflows/reactive-average-example-mean.bonsai)
:::

> [!NOTE]
> The [`Delay`](xref:Bonsai.Reactive.Delay) operator is used in this example only to keep the workflow open long enough to visualize the result. Since only a single value is emitted, use an [`ObjectTextVisualizer`](xref:Bonsai.Design.ObjectTextVisualizer) to visualize it.

Use `Average` to implement a moving average by placing it inside a [`SelectMany`](xref:Bonsai.Reactive.SelectMany) to report the mean for sliding windows created by [`WindowCount`](xref:Bonsai.Reactive.WindowCount).

:::workflow
![Moving Average](../workflows/reactive-average-example-moving-average.bonsai)
:::

Use `Average` to downsample a signal by placing it inside a [`SelectMany`](xref:Bonsai.Reactive.SelectMany) to report the mean for non-overlapping windows created by [`WindowCount`](xref:Bonsai.Reactive.WindowCount).

:::workflow
![Downsample](../workflows/reactive-average-example-downsample.bonsai)
:::

### Alternative
Use [`Accumulate`](xref:Bonsai.Reactive.Accumulate) instead to implement a cumulative average by dividing the accumulated value using the element count from [`ElementIndex`](xref:Bonsai.Reactive.ElementIndex).

:::workflow
![Downsample](../workflows/reactive-average-alternative-cumulative-average.bonsai)
:::