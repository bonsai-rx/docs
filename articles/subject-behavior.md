---
uid: subject-behavior
title: "BehaviorSubject"
---

![Marble diagram](~/images/language-subject-behavior.svg)

[`BehaviorSubject`] stores and passes the latest value emitted by the source sequence to each subscribed observer, and then continues to emit any subsequent values.

Any observers which subscribe later will immediately receive the latest stored value. However, if the source sequence terminates with an error, [`BehaviorSubject`] will not emit any values but will pass along the error notification to all subsequent observers.

> [!Warning]
> [`BehaviorSubject`] is designed to multicast and share state updates from multiple sources, like a global variable. Because of this, even if one of the source sequences emitting values to [`BehaviorSubject`] terminates successfully, the [`BehaviorSubject`] will not send a termination message to any subscribed observers, but will remain active until the enclosing workflow scope is terminated to allow other sources to update the shared state.

<!-- Reference-style links -->
[`BehaviorSubject`]: xref:Bonsai.Reactive.BehaviorSubject