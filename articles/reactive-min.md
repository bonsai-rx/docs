---
uid: reactive-min
title: Min
---

![Marble diagram](~/images/reactive-min.svg)

The `Min` operator collects all the values from the source sequence and emits a single value representing the smallest of all values. The single result value is emitted only when the source sequence terminates successfully.

### Examples

Use `Min` to report the smallest value at the end of the sequence.

:::workflow
![Min Example](../workflows/reactive-min-example.bonsai)
:::