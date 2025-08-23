---
uid: reactive-repeat
title: Repeat
---

![Marble diagram](~/images/reactive-repeat.svg)

`Repeat` reacts to successful termination by disposing the previous subscription and resubscribing to the source sequence. Elements received from all of the subscriptions are forwarded to the result sequence.

If any of the subscriptions terminates exceptionally, the result sequence will also terminate exceptionally, and no further resubscriptions will be made.

[!include[Resubscription](~/articles/reactive-resubscription.md)]

### Example

Use `Repeat` to repeat an observable sequence indefinitely.

:::workflow
![Repeat Example](../workflows/reactive-repeat-example.bonsai)
:::

### Alternative

Use [`RepeatCount`](xref:Bonsai.Reactive.RepeatCount) to repeat an observable sequence a specified number of times.