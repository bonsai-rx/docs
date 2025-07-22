---
uid: reactive-skipuntil
title: SkipUntil
---

![Marble diagram](~/images/reactive-skipuntil.svg)

`SkipUntil` modifies the source sequence so that all elements are ignored until the second sequence produces a notification. At that time, `SkipUntil` will start emitting all remaining elements from the source sequence. `SkipUntil` is often used to create a dynamic start condition for an infinite sequence.

If the source sequence terminates before the second sequence produces a value, `SkipUntil` will terminate without emitting any elements.

### Examples

Use `SkipUntil` to skip elements from an active sequence.

:::workflow
![SkipUntil Example](../workflows/reactive-skipuntil-example.bonsai)
:::

#### Start Video Recording

Use `SkipUntil` to start video recording when a trigger is sent (e.g. key press).

:::workflow
![SkipUntil Application Start Video Recording](../workflows/reactive-skipuntil-application-videostart.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Vision`, `Bonsai.Vision.Design`, and `Bonsai.Windows.Input` packages to be installed. 

> [!NOTE]
> Use [`TakeUntil`](xref:Bonsai.Reactive.TakeUntil) to control the termination of video recording.

### Alternative

Use [`SubscribeWhen`](xref:Bonsai.Reactive.SubscribeWhen) to control the start of subscription.

> [!Warning]
> Although `SubscribeWhen` and `SkipUntil` often produce a similar sequence, `SkipUntil` always subscribes to the source sequence immediately. This means that any initialization side-effects will be evaluated immediately. For *hot* sequences (e.g. camera) this might be advantageous, since any initialization costs are paid upfront, and new values are immediately ready to be consumed after the trigger. However, for *cold* sequences (e.g. video or a timer) this might lead to loss of data from the start of the sequence. For more about the difference between *hot* and *cold* sequences, see the section on [temperature](xref:observables#temperature).