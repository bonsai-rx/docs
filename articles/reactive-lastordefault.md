---
uid: reactive-lastordefault
title: LastOrDefault
---

![Marble diagram](~/images/reactive-lastordefault.svg)

If the sequence has no elements, `LastOrDefault` will emit a default value before terminating successfully. This is a subtle but important difference between the `LastOrDefault` operator and [`TakeLast(1)`](xref:Bonsai.Reactive.TakeLast), which will also complete successfully when the source sequence is empty, but will not emit any values.

> [!Tip]
> `LastOrDefault` is one of the simplest and most efficient ways of capturing the end of an observable sequence explicitly as a notification in the workflow. You can use it to react to the termination of a sequence regardless of whether that sequence produces values.
