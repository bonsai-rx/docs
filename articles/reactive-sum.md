---
uid: reactive-sum
title: Sum
---

![Marble diagram](~/images/reactive-sum.svg)

The `Sum` operator collects all the numbers from the source sequence and emits a single value representing the sum of all numbers. The single result value is emitted only when the source sequence terminates successfully.

### Example

Use `Sum` to report the total value at the end of a sequence.

:::workflow
![Sum Example](../workflows/reactive-sum-example.bonsai)
:::

### Alternative

Use [`Accumulate`](xref:Bonsai.Reactive.Accumulate) instead to continuously track the value in the sequence.