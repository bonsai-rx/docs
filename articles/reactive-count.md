---
uid: reactive-count
title: Count
---

![Marble diagram](~/images/reactive-count.svg)

The `Count` operator collects all the values from the source sequence and emits a single value representing the total number of items. The single result value is emitted only when the source sequence terminates successfully.

### Example
Use `Count` to report the total count of elements at the end of a sequence.

:::workflow
![Total count](../workflows/reactive-count-example.bonsai)
:::

### Alternative
Use [`ElementIndex`](xref:Bonsai.Reactive.ElementIndex) instead to continuously track the number of elements in the sequence.