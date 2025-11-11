---
uid: reactive-distinctuntilchangedby
title: DistinctUntilChangedBy
---

![Marble diagram](~/images/reactive-distinctuntilchangedby.svg)

The `DistinctUntilChangedBy` operator removes all contiguous elements in the sequence with equal keys. The <xref href="Bonsai.Reactive.DistinctUntilChangedBy.KeySelector"/> property specifies the member, or set of members, used to test whether elements in the source sequence are equal. Equality is determined by the default <xref href="System.Collections.Generic.EqualityComparer`1"/> for the type of the selected key.

In other words, after each element is emitted by the result sequence, subsequent elements will be dropped until the value of the key changes.

### Examples

Use `DistinctUntilChangedBy` to return non-contiguous distinct elements as determined by the specified key.

:::workflow
![DistinctUntilChangedBy Example](../workflows/reactive-distinctuntilchangedby-example.bonsai)
:::