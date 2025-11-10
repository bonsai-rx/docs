---
uid: reactive-sampleinterval
title: SampleInterval
---

![Marble diagram](~/images/reactive-sampleinterval.svg)

If multiple elements are received during each sampling period, `SampleInterval` will emit only the latest value. However, elements are never repeated: if no new elements are received between two sampling events, no notification will be emitted when the sampling period elapses.

### Examples

Use `SampleInterval` to extract the latest element from a source sequence that is emitted within within the time interval.

:::workflow
![SampleInterval Example](../workflows/reactive-sampleinterval-example.bonsai)
:::

### Related Operators

Use [`GateInterval`](xref:Bonsai.Reactive.GateInterval) to extract the first element from a source sequence that is emitted within the time interval.

Use [`Slice`](xref:Bonsai.Reactive.Slice) to extract elements based on element count instead of time.

Use [`Sample`](xref:Bonsai.Reactive.Sample) to extract elements based on notifications from another sequence.