---
uid: reactive-thenby
title: ThenBy
---

![Marble diagram](~/images/reactive-thenby.svg)

`ThenBy` operates on sequences returned by any of the <xref href="Bonsai.Reactive.OrderBy"/>, <xref href="Bonsai.Reactive.OrderByDescending"/>, <xref href="Bonsai.Reactive.ThenBy"/>, or <xref href="Bonsai.Reactive.ThenByDescending"/> operators. For each ordered collection emitted by the source sequence, the result sequence will emit a new ordered collection where elements in the collection are subsequently sorted in ascending order of the keys specified in the <xref href="Bonsai.Reactive.ThenBy.KeySelector"/> property.

[!include[LazyOrdering](~/articles/reactive-lazyordering.md)]

### Examples

Use `ThenBy` to perform a ascending sort on ordered collections according to the specified key.

:::workflow
![ThenBy Example](../workflows/reactive-thenby-example.bonsai)
:::