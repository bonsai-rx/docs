---
uid: reactive-accumulate
title: Accumulate
---

![Marble diagram](~/images/reactive-accumulate.svg)

The `Accumulate` operator returns the current value of the cumulative sum each time the source sequence emits a notification. The result sequence terminates successfully when the source sequence terminates successfully.

### Example

Use `Accumulate` to continuously update a value by adding up the changes over time.

:::workflow
![Accumulate Example](../workflows/reactive-accumulate-example.bonsai)
:::

### Related Operators

Use [`Sum`](xref:Bonsai.Reactive.Sum) instead to yield a single accumulated value at the end of a sequence.