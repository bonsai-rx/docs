---
uid: reactive-dematerialize
title: Dematerialize
---

![Marble diagram](~/images/reactive-dematerialize.svg)

`Dematerialize` is the complement of <xref href="Bonsai.Reactive.Materialize"/>. `Dematerialize` reconstructs the implicit notifications of an observable sequence from a sequence of explicit notifications. This can be useful if you have materialized a sequence for debugging or logging purposes but still need to retain the original sequence.

### Example

Use `Dematerialize` to convert explicit notifications back to implicit notifications.

:::workflow
![Dematerialize Example](../workflows/reactive-dematerialize-example.bonsai)
:::