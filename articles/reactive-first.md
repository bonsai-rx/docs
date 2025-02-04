---
uid: reactive-first
title: First
---

![Marble diagram](~/images/reactive-first.svg)

If the sequence has no elements, `First` will terminate with an error.

> [!Tip]
> If you are interested in finding the first element that meets some criteria, consider using the [`Condition`](xref:Bonsai.Reactive.Condition) operator before `First`.

> [!Warning]
> There are subtle but important differences between using the `First` operator and [`Take(1)`](xref:Bonsai.Reactive.Take):
>   - When the source sequence has no elements, `Take(1)` will complete successfully, while `First` will throw an error.
>   - When the source sequence emits the first element, `Take(1)` will immediately cancel the subscription to the source sequence before emitting the notification. `First`, on the other hand, will emit the notification and only afterwards cancel the subscription to the source sequence.
