---
uid: reactive-subscribewhen
title: SubscribeWhen
---

![Marble diagram](~/images/reactive-subscribewhen.svg)

The `SubscribeWhen` operator modifies the source sequence by waiting for the first value emitted by the second sequence before subscribing to the first sequence. This has the effect of delaying the start of the sequence until the second sequence emits a value.

`SubscribeWhen` can be used to control the timing of initialization. Note that if a source is [*hot*](xref:observables#temperature), delaying the start of the sequence will not preserve past data.
