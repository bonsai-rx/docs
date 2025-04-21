---
uid: reactive-skipuntil
title: SkipUntil
---

![Marble diagram](~/images/reactive-skipuntil.svg)

`SkipUntil` modifies the source sequence so that all elements are ignored until the second sequence produces a notification. At that time, `SkipUntil` will start emitting all remaining elements from the source sequence. 

If the source sequence terminates before the second sequence produces a value, `SkipUntil` will terminate without emitting any elements.

### Examples

Use `SkipUntil` to create a dynamic start condition for an infinite sequence.

:::workflow
![SkipUntil Example](../workflows/reactive-skipuntil-example.bonsai)
:::

#### Start Video Recording

Use `SkipUntil` to start video recording when a trigger is sent (e.g. key press).

:::workflow
![SkipUntil Application Start Video Recording](../workflows/reactive-skipuntil-application-videostart.bonsai)
:::

> [!Note]
> Use [`TakeUntil`](xref:Bonsai.Reactive.TakeUntil) to control when video recording stops.

### Alternative

Use [`SubscribeWhen`](xref:Bonsai.Reactive.SubscribeWhen) to control the start of subscription.

> [!Warning]
> Although often both `SubscribeWhen` and `SkipUntil` result in a similar sequence, `SkipUntil` will always immediately subscribe to the source sequence. This means that any initialization side-effects will be evaluated immediately. For *hot* sequences (e.g. camera) this might be advantageous, since any initialization costs are paid upfront, and new values are immediately ready to be consumed after the trigger. However, for *cold* sequences (e.g. video) this might lead to loss of data from the start of the sequence. For more about the difference between *hot* and *cold* sequences, see the section on [temperature](xref:observables#temperature).
