---
uid: reactive-delay
title: Delay
---

![Marble diagram](~/images/reactive-delay.svg)

The `Delay` operator modifies the source sequence by pausing for the specified duration before emitting each of the notifications in the original sequence. This has the effect of delaying the timing of the entire sequence of notifications by that specified time interval.

`Delay` is useful to model delayed responses to events in a control task, but also to access past data from a continuous stream in the future. In other words, if the stream timing is delayed, then any downstream observers grabbing data in the present moment will be receiving notifications from the past. For example, if you are recording data aligned on a temporal trigger detected in real-time, you can record data before the trigger simply by triggering the delayed sequence.

### Examples

Use `Delay` to postpone emission of elements from an observable sequence.

:::workflow
![Delay Example](../workflows/reactive-delay-example.bonsai)
:::

### Related Operators

Use [`DelaySubscription`](xref:Bonsai.Reactive.DelaySubscription) to delay initialization of an observable sequence.
