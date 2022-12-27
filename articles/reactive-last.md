---
uid: reactive-last
title: Last
---

![Marble diagram](~/images/reactive-last.svg)

If the sequence has no elements, `Last` will terminate with an error. This is a subtle but important difference between the `Last` operator and [`TakeLast(1)`](xref:Bonsai.Reactive.TakeLast), which will complete successfully when the source sequence has no elements.
