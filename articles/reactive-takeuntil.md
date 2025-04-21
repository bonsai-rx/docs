---
uid: reactive-takeuntil
title: TakeUntil
---

![Marble diagram](~/images/reactive-takeuntil.svg)

`TakeUntil` modifies the source sequence so that values are emitted only until the second sequence produces a value. At that time, `TakeUntil` will terminate immediately and ignore the remainder of the sequence. 

If the source sequence terminates before the second sequence produces a value, `TakeUntil` will also terminate and cancel the subscription to the second sequence.

### Examples

Use `TakeUntil` to stop taking elements from an active sequence.

:::workflow
![TakeUntil Example](../workflows/reactive-takeuntil-example.bonsai)
:::

#### Stop Video Recording

Use `TakeUntil` to stop video recording when a trigger is sent (e.g. key press).

:::workflow
![TakeUntil Application Stop Video Recording](../workflows/reactive-takeuntil-application-videostop.bonsai)
:::

> [!Note]
> Use [`SkipUntil`](xref:Bonsai.Reactive.SkipUntil) to control the start of video recording.