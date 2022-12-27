---
uid: reactive-distinct
title: Distinct
---

![Marble diagram](~/images/reactive-distinct.svg)

The `Distinct` operator ensures that only unique elements are included in the result sequence. Uniqueness is specified by the default <xref href="System.Collections.Generic.EqualityComparer`1"/> for the type of the elements in the source sequence. If multiple non-unique elements are present in the source sequence, only the first element will be included in the result sequence.
