---
uid: reactive-accumulate
title: Accumulate
---

![Marble diagram](~/images/reactive-accumulate.svg)

The `Accumulate` operator returns the current value of the cumulative sum each time the source sequence emits a notification. The result sequence terminates successfully when the source sequence terminates successfully.

### Example

Use `Accumulate` to continuously track a value by adding up the changes over time in a sequence.

:::workflow
![Accumulate Example](../workflows/reactive-accumulate-example.bonsai)
:::

### Alternative

Use [`Sum`](xref:Bonsai.Reactive.Sum) instead to yield a single value at the end of a sequence.