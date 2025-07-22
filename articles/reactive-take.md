---
uid: reactive-take
title: Take
---

![Marble diagram](~/images/reactive-take.svg)

The `Take` operator modifies the source sequence to emit only the specified maximum number of values from the start of the sequence. If the maximum number of values is reached, `Take` will terminate immediately and ignore the remainder of the sequence. `Take` is commonly used to convert an infinite sequence into a finite sequence, for example to take the first key press out of an infinite sequence of keyboard key presses.

`Take` only specifies a maximum upper bound on the number of elements. If the source sequence terminates before that maximum number of values is reached, the behavior of the sequence will not be modified.

### Example

Use `Take` to retrieve one or more elements from the start of a sequence.

:::workflow
![Take Example](../workflows/reactive-take-example.bonsai)
:::

### Alternative

Use [`First`](xref:Bonsai.Reactive.First) to retrieve the first element from the start of a sequence.

> [!Warning]
> There are subtle but important differences between using the `Take(1)` and [`First`](xref:Bonsai.Reactive.First) operator:
>   - When the source sequence has no elements, `Take(1)` will complete successfully, while [`First`](xref:Bonsai.Reactive.First) will throw an error.
>   - When the source sequence emits the first element, `Take(1)` will immediately cancel the subscription to the source sequence before emitting the notification. [`First`](xref:Bonsai.Reactive.First), on the other hand, will emit the notification and only afterwards cancel the subscription to the source sequence.

