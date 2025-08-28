---
uid: reactive-thenbydescending
title: ThenByDescending
---

![Marble diagram](~/images/reactive-thenbydescending.svg)

`ThenByDescending` operates on sequences returned by any of the <xref href="Bonsai.Reactive.OrderBy"/>, <xref href="Bonsai.Reactive.OrderByDescending"/>, <xref href="Bonsai.Reactive.ThenBy"/>, or <xref href="Bonsai.Reactive.ThenByDescending"/> operators. For each ordered collection emitted by the source sequence, the result sequence will emit a new ordered collection where elements in the collection are subsequently sorted in descending order of the keys specified in the <xref href="Bonsai.Reactive.ThenByDescending.KeySelector"/> property.

[!include[LazyOrdering](~/articles/reactive-lazyordering.md)]

### Example

Use `ThenByDescending` to perform a descending sort on ordered collections according to the specified key.

:::workflow
![ThenByDescending Example](../workflows/reactive-thenbydescending-example.bonsai)
:::