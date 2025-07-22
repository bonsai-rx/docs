---
uid: reactive-delaysubscription
title: DelaySubscription
---

![Marble diagram](~/images/reactive-delaysubscription.svg)

The `DelaySubscription` operator modifies the source sequence by pausing for the specified duration before subscribing to the original sequence. This has the effect of delaying the start of the sequence by the specified time interval.

`DelaySubscription` can be used to control the timing of initialization. Note that if a source is [*hot*](xref:observables#temperature), delaying the start of the sequence will not preserve past data, since unlike [`Delay`](xref:Bonsai.Reactive.Delay) the `DelaySubscription` operator does not store or have access to any historical data.

### Example

Use `DelaySubscription` to delay initialization of an observable sequence.

:::workflow
![DelaySubscription Example](../workflows/reactive-delaysubscription-example.bonsai)
:::

### Alternative

Use [`Delay`](xref:Bonsai.Reactive.Delay) to access past data from [*hot*](xref:observables#temperature) sequences or delay notifications of an observable sequence.