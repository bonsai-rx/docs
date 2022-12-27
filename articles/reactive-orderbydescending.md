---
uid: reactive-orderbydescending
title: OrderByDescending
---

![Marble diagram](~/images/reactive-orderbydescending.svg)

The `OrderByDescending` operator requires the elements in the source sequence to be collections implementing the <xref href="System.Collections.Generic.IEnumerable`1"/> interface. For each collection emitted by the source sequence, the result sequence will emit an ordered collection where elements are sorted in descending order of the keys specified in the <xref href="Bonsai.Reactive.OrderByDescending.KeySelector"/> property.

[!include[LazyOrdering](~/articles/reactive-lazyordering.md)]
