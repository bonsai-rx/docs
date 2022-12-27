---
uid: reactive-gateinterval
title: GateInterval
---

![Marble diagram](~/images/reactive-gateinterval.svg)

The gate starts in the open state, and a single element is allowed to pass through from the source sequence. After this first element is emitted, the gate closes and all subsequent elements are dropped from the result sequence. The gate reopens when the specified <xref href="Bonsai.Reactive.GateInterval.Interval"/> elapses.

It is possible to specify how long the gate stays open by using the <xref href="Bonsai.Reactive.GateInterval.DueTime"/> property. If no value is specified, the gate stays open indefinitely until an element arrives. If a maximum due time is specified, then no elements from the source sequence arriving after the due time elapses will be allowed through until the gate reopens.
