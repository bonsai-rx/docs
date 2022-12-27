---
uid: reactive-distinctby
title: DistinctBy
---

![Marble diagram](~/images/reactive-distinctby.svg)

The `DistinctBy` operator ensures that only unique elements are included in the result sequence. The <xref href="Bonsai.Reactive.DistinctBy.KeySelector"/> property specifies the member, or set of members, to use to test the uniqueness of each element in the source sequence. The default <xref href="System.Collections.Generic.EqualityComparer`1"/> for the type of the selected key is used to check whether each key is unique. If multiple non-unique keys are present in the source sequence, only the first element emitted with a given key will be included in the result sequence.
