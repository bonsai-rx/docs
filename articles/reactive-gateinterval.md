---
uid: reactive-gateinterval
title: GateInterval
---

![Marble diagram](~/images/reactive-gateinterval.svg)

The gate starts in the open state, and a single element is allowed to pass through from the source sequence. After this first element is emitted, the gate closes and all subsequent elements are dropped from the result sequence. The gate reopens when the specified <xref href="Bonsai.Reactive.GateInterval.Interval"/> elapses.

It is possible to specify how long the gate stays open by using the <xref href="Bonsai.Reactive.GateInterval.DueTime"/> property. If no value is specified, the gate stays open indefinitely until an element arrives. If a maximum due time is specified, then no elements from the source sequence arriving after the due time elapses will be allowed through until the gate reopens.

### Examples

Use `GateInterval` to extract the first element from a source sequence that is emitted within the time interval.

:::workflow
![GateInterval Example](../workflows/reactive-gateinterval-example.bonsai)
:::

### Related Operators

Use [`SampleInterval`](xref:Bonsai.Reactive.SampleInterval) to extract the latest element from a source sequence that is emitted within the time interval.

Use [`Slice`](xref:Bonsai.Reactive.Slice) to extract elements based on element count instead of time.

Use [`Gate`](xref:Bonsai.Reactive.Gate) to gate elements based on the notifications from another sequence.