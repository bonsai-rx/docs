---
uid: reactive-retrycount
title: RetryCount
---

![Marble diagram](~/images/reactive-retrycount.svg)

`RetryCount` reacts to exceptional termination by disposing the previous subscription and resubscribing to the source sequence, up to the maximum number of times specified in the <xref href="Bonsai.Reactive.RetryCount.Count"/> property. Value notifications received from all of the subscriptions are forwarded to the result sequence.

After the source sequence terminates exceptionally the specified maximum number of times, the result sequence will also terminate exceptionally. If any of the subscriptions completes successfully, the result sequence will also complete, and no further resubscriptions will be made.

[!include[Resubscription](~/articles/reactive-resubscription.md)]

### Example

Use `RetryCount` to repeat subscription to an observable sequence a specified number of times.

:::workflow
![RetryCount Example](../workflows/reactive-retrycount-example.bonsai)
:::

### Related Operators

Use [`Retry`](xref:Bonsai.Reactive.RetryCount) instead to repeat subscription to an observable sequence until it terminates successfully, without limit on retries.