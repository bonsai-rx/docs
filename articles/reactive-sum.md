---
uid: reactive-sum
title: Sum
---

![Marble diagram](~/images/reactive-sum.svg)

The `Sum` operator collects all the numbers from the source sequence and emits a single value representing the sum of all numbers. The single result value is emitted only when the source sequence terminates successfully.

### Example
Use `Sum` to report the total value at the end of a sequence.

:::workflow
![Total value](../workflows/reactive-sum-example.bonsai)
:::

> [!NOTE]
> The [`Delay`](xref:Bonsai.Reactive.Delay) operator is used in this example only to keep the workflow open long enough to visualize the result. Since only a single value is emitted, use an [`ObjectTextVisualizer`](xref:Bonsai.Design.ObjectTextVisualizer) to visualize it.

### Alternative
Use [`Accumulate`](xref:Bonsai.Reactive.Accumulate) instead to continuously track the value in the sequence.