---
uid: reactive-observeon
title: ObserveOn
---

An observable sequence, and the chain of operators that are applied to it, will usually do its work and notify any downstream observers on the same thread that is used to run the source. The `ObserveOn` operator can be used to instruct a sequence to send notifications to its observers on a particular scheduler.

![Marble diagram](~/images/reactive-observeon.svg)

`ObserveOn` will change the thread used to send notifications only for items emitted downstream from where the operator is introduced. Even if new tasks or threads are created to run notifications, the resulting sequence will keep the order of all emitted items.

> [!Warning]
> Care must be taken to prevent unbounded accumulation of notifications when consumers following `ObserveOn` are slower than the rate at which the source produces new items. Reactive operators such as [`Gate`](xref:Bonsai.Reactive.Gate) or [`Slice`](xref:Bonsai.Reactive.Slice) may be used to manage any backpressure issues.

![Marble diagram](~/images/reactive-observeon-error.svg)

Note that `ObserveOn` will forward any error notification from the source sequence immediately, without waiting for slow-consuming observers to receive previously emitted items. In other words, the error notification may jump ahead of items emitted earlier by the source sequence as in the diagram above.
