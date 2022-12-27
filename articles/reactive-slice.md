---
uid: reactive-slice
title: Slice
---

![Marble diagram](~/images/reactive-slice.svg)

The `Slice` operator specifies an index-based filter over elements of the source sequence. Elements from the source sequence are accepted if their index is: greater than or equal to <xref href="Bonsai.Reactive.Slice.Start"/>; less than <xref href="Bonsai.Reactive.Slice.Stop"/>, or the stop index property is not specified; not set to be skipped by the <xref href="Bonsai.Reactive.Slice.Step"/> property.

> [!Warning]
> If the index of elements in the source sequence becomes greater than or equal to <xref href="Bonsai.Reactive.Slice.Stop"/>, then `Slice` will terminate successfully and cancel the subscription to the source sequence.
