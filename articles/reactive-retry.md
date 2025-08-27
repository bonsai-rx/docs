---
uid: reactive-retry
title: Retry
---

![Marble diagram](~/images/reactive-retry.svg)

`Retry` reacts to exceptional termination by disposing the previous subscription and resubscribing to the source sequence. Elements received from all of the subscriptions are forwarded to the result sequence.

If any of the subscriptions completes successfully, the result sequence will also complete, and no further resubscriptions will be made.

[!include[Resubscription](~/articles/reactive-resubscription.md)]

### Example

Use `Retry` to repeat subscription to an observable sequence if it terminates with an exception.

:::workflow
![Retry Example](../workflows/reactive-retry-example.bonsai)
:::

### Alternative

Use [`RetryCount`](xref:Bonsai.Reactive.RetryCount) to repeat subscription to an observable sequence a specified number of times.