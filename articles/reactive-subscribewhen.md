---
uid: reactive-subscribewhen
title: SubscribeWhen
---

![Marble diagram](~/images/reactive-subscribewhen.svg)

The `SubscribeWhen` operator modifies the source sequence by waiting for the first value emitted by the second sequence before subscribing to the first sequence. This has the effect of delaying the start of the sequence until the second sequence emits a value.

`SubscribeWhen` can be used to control the timing of initialization. Note that if a source is [*hot*](xref:observables#temperature), delaying the start of the sequence will not preserve past data.

### Example

Use `SubscribeWhen` to start subscription to a sequence.

:::workflow
![SubscribeWhen Example](../workflows/reactive-subscribewhen-example.bonsai)
:::

### Related Operators

Use [`SkipUntil`](xref:Bonsai.Reactive.SkipUntil) to skip elements from an active subscription.

> [!Warning]
> Although `SubscribeWhen` and `SkipUntil` often produce a similar sequence, `SubscribeWhen` only subscribes to the source sequence when triggered. This means that any initialization side-effects will be delayed. For *hot* sequences (e.g. camera) this might be disadvantageous as initialization costs are paid upon subscription, and new values after the trigger are not immediately available. However, for *cold* sequences (e.g. video or a timer) this might be beneficial, as all data from the start of the sequence will be available. For more about the difference between *hot* and *cold* sequences, see the section on [temperature](xref:observables#temperature).