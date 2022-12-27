---
uid: reactive-subscribeon
title: SubscribeOn
---

An observable sequence, and the chain of operators that are applied to it, will often do its work and notify any downstream observers on the same thread on which the subscribe action is called. The `SubscribeOn` operator changes this behavior by specifying a different scheduler for the subscribe (and unsubscribe) action.

![Marble diagram](~/images/reactive-subscribeon.svg)

As shown in the diagram, the `SubscribeOn` operator can affect the ultimate source of notifications, no matter where in the chain of operators it is placed, as it changes the thread for the entire upstream subscribe call. By contrast, the [`ObserveOn`](xref:Bonsai.Reactive.ObserveOn) operator changes only the scheduler on which notifications are sent, which affects only downstream operators.

> [!Warning]
> Hot observable sources such as hardware devices often impose their own execution schedulers, e.g. by hooking notifications to device driver callbacks or interrupts. In these situations it is usually more appropriate to control concurrency using the [`ObserveOn`](xref:Bonsai.Reactive.ObserveOn) operator.
