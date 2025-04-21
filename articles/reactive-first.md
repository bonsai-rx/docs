---
uid: reactive-first
title: First
---

![Marble diagram](~/images/reactive-first.svg)

If the sequence has no elements, `First` will terminate with an error.

> [!Tip]
> If you are interested in finding the first element that meets some criteria, consider using the [`Condition`](xref:Bonsai.Reactive.Condition) operator before `First`.

### Example

Use `First` to retrieve the first element of a sequence.

:::workflow
![First Example](../workflows/reactive-first-example.bonsai)
:::

### Alternative

Use [`Take`](xref:Bonsai.Reactive.Take) to retrieve one or more elements from the start of the sequence.

> [!Warning]
> There are subtle but important differences between using the `First` operator and [`Take(1)`](xref:Bonsai.Reactive.Take):
>   - When the source sequence has no elements, [`Take(1)`](xref:Bonsai.Reactive.Take) will complete successfully, while `First` will throw an error.
>   - When the source sequence emits the first element, [`Take(1)`](xref:Bonsai.Reactive.Take) will immediately cancel the subscription to the source sequence before emitting the notification. `First`, on the other hand, will emit the notification and only afterwards cancel the subscription to the source sequence.