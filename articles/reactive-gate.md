---
uid: reactive-gate
title: Gate
---

![Marble diagram](~/images/reactive-gate.svg)

When the gate is in the open state, a single element is allowed to pass through from the source sequence. After this first element is emitted, the gate closes and all subsequent elements are dropped from the result sequence. The gate reopens when the second sequence emits a notification. 

It is possible to specify how long the gate stays open by using the <xref href="Bonsai.Reactive.Gate.DueTime"/> property. If no value is specified, the gate stays open indefinitely until an element arrives. In this case, the gate starts immediately in the open state.

If a maximum due time is specified, no elements from the source sequence arriving after the due time elapses will be allowed through and the gate may close again without emitting any new elements. In this case, the gate starts in the closed state, and only opens when the second sequence emits a notification.

> [!Warning]
> If the second sequence emits notifications before the gate is closed, the gate will remain open. If there is a maximum specified due time, the timer will be reset upon arrival of the new notification. Even if there are multiple opening notifications, only a single element can make it through the gate.
