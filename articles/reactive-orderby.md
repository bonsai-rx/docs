---
uid: reactive-orderby
title: OrderBy
---

![Marble diagram](~/images/reactive-orderby.svg)

The `OrderBy` operator requires the elements in the source sequence to be collections implementing the <xref href="System.Collections.Generic.IEnumerable`1"/> interface. For each collection emitted by the source sequence, the result sequence will emit an ordered collection where elements are sorted in ascending order of the keys specified in the <xref href="Bonsai.Reactive.OrderBy.KeySelector"/> property.

[!include[LazyOrdering](~/articles/reactive-lazyordering.md)]

### Examples

Use `OrderBy` to sort elements in ascending order according to the specified key.

:::workflow
![OrderBy Example](../workflows/reactive-orderby-example.bonsai)
:::