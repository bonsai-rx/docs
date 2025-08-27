---
uid: reactive-materialize
title: Materialize
---

![Marble diagram](~/images/reactive-materialize.svg)

`Materialize` surfaces all notifications in the source sequence as explicit values, including termination messages (<xref href="System.IObserver`1.OnError*"/> and <xref href="System.IObserver`1.OnCompleted*"/>). Converting termination messages into explicit notifications can be useful to reveal the entire behavior of a sequence for debugging or logging purposes.

The application of `Materialize` can be reversed by applying <xref href="Bonsai.Reactive.Dematerialize"/> to the result sequence.

### Example

Use `Materialize` to surface implicit notifications as explicit notifications.

:::workflow
![Materialize Example](../workflows/reactive-materialize-example.bonsai)
:::