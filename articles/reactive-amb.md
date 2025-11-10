---
uid: reactive-amb
title: Amb
---

![Marble diagram](~/images/reactive-amb.svg)

The `Amb` operator sets up a winner-take-all race condition between all source sequences. The first sequence to emit a notification will gain full control of the output, and all the other sequences will have their subscriptions immediatelly cancelled. `Amb` is most commonly used to ensure only one of many outcomes being evaluated in parallel is propagated.

### Examples

Use `Amb` to propagate the first observable sequence to emit a notification.

:::workflow
![Amb Example](../workflows/reactive-amb-example.bonsai)
:::

### Related Operators

Use [`Switch`](xref:Bonsai.Reactive.Switch) instead to propagate the latest observable sequence that emits notifications from a sequence of observable sequences.