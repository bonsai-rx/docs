---
uid: reactive-takelast
title: TakeLast
---

![Marble diagram](~/images/reactive-takelast.svg)

The `TakeLast` operator modifies the source sequence to emit only a specified maximum number of values from the end of the sequence. Since `TakeLast` does not know which elements are the last before the original sequence terminates, it will not emit any value until the completion event is emitted, but will instead keep in memory the specified number of "latest" values. At the time when the source sequence terminates, `TakeLast` will immediately emit all buffered values up to the specified maximum number of elements and then terminate.

Because of this buffering behavior, `TakeLast` will always modify the behavior of the original sequence, regardless of how many values it contains.

### Example

Use `TakeLast` to retrieve one or more elements from the start of a sequence.

:::workflow
![TakeLast Example](../workflows/reactive-takelast-example.bonsai)
:::

### Alternative

Use [`Last`](xref:Bonsai.Reactive.Last) to retrieve the last element from the end of the sequence.

> [!Warning]
> There is a subtle but important difference between the `TakeLast(1)` and [`Last`](xref:Bonsai.Reactive.Last) operator. `TakeLast(1)` will complete successfully when the source sequence has no elements but [`Last`](xref:Bonsai.Reactive.Last) will terminate with an error. 