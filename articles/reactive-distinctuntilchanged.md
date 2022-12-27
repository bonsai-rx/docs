---
uid: reactive-distinctuntilchanged
title: DistinctUntilChanged
---

![Marble diagram](~/images/reactive-distinctuntilchanged.svg)

The `DistinctUntilChanged` operator removes all contiguous elements in the sequence that are equal. Equality is determined by the default <xref href="System.Collections.Generic.EqualityComparer`1"/> for the type of the elements in the source sequence.

In other words, after each element is emitted by the result sequence, subsequent elements will be dropped until the value changes.
