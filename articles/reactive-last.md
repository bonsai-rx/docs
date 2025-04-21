---
uid: reactive-last
title: Last
---

![Marble diagram](~/images/reactive-last.svg)

If the sequence has no elements, `Last` will terminate with an error. 

### Example

Use `Last` to retrieve the last element of a sequence.

:::workflow
![Last Example](../workflows/reactive-last-example.bonsai)
:::

### Alternative

Use [`TakeLast`](xref:Bonsai.Reactive.TakeLast) to retrieve one or more elements from the end of the sequence.

> [!Warning]
> There is a subtle but important difference between the `Last` operator and [`TakeLast(1)`](xref:Bonsai.Reactive.TakeLast). [`TakeLast(1)`](xref:Bonsai.Reactive.TakeLast)  will complete successfully when the source sequence has no elements.
