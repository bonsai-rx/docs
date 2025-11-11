---
uid: reactive-sum
title: Sum
---

![Marble diagram](~/images/reactive-sum.svg)

The `Sum` operator collects all the numbers from the source sequence and emits a single value representing the sum of all numbers. The single result value is emitted only when the source sequence terminates successfully.

### Examples

Use `Sum` to report the sum of all elements at the end of a sequence.

:::workflow
![Sum Example](../workflows/reactive-sum-example.bonsai)
:::

### Related Operators

Use [`Accumulate`](xref:Bonsai.Reactive.Accumulate) instead to continuously track the running sum of values in the sequence.