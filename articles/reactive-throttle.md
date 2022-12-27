---
uid: reactive-throttle
title: Throttle
---

![Marble diagram](~/images/reactive-throttle.svg)

The `Throttle` operator provides a mechanism to control backpressure in reactive streams. `Throttle` emits an element from the source sequence only if that element is followed by a period of silence longer than <xref href="Bonsai.Reactive.Throttle.DueTime"/>. If new elements are received during this period, the previous element is dropped and the silent period timer is reset.
