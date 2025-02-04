---
uid: reactive-firstordefault
title: FirstOrDefault
---

![Marble diagram](~/images/reactive-firstordefault.svg)

If the sequence has no elements, `FirstOrDefault` will emit a default value before terminating successfully.

> [!Tip]
> If you are interested in finding the first element that meets some criteria, consider using the [`Condition`](xref:Bonsai.Reactive.Condition) operator before `FirstOrDefault`.

> [!Warning]
> There are subtle but important differences between using the `FirstOrDefault` operator and [`Take(1)`](xref:Bonsai.Reactive.Take):
>   - When the source sequence has no elements, `Take(1)` will complete successfully with no emitted values, while `FirstOrDefault` will emit a default value before terminating successfully.
>   - When the source sequence emits the first element, `Take(1)` will immediately cancel the subscription to the source sequence before emitting the notification. `FirstOrDefault`, on the other hand, will emit the notification and only afterwards cancel the subscription to the source sequence.
