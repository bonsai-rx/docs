---
uid: reactive-max
title: Max
---

![Marble diagram](~/images/reactive-max.svg)

The `Max` operator collects all the values from the source sequence and emits a single value representing the largest of all values. The single result value is emitted only when the source sequence terminates successfully.

### Example

Use `Max` to report the maximum value at the end of the sequence.

:::workflow
![Max Example](../workflows/reactive-max-example.bonsai)
:::