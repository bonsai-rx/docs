---
uid: reactive-groupby
title: GroupBy
---

![Marble diagram](~/images/reactive-groupby.svg)

The `GroupBy` operator can be used to separate, or demultiplex, the elements from a single sequence into multiple sequences according to the specified 
<xref href="Bonsai.Reactive.GroupBy.KeySelector"/>. Each element from the sequence will be routed to the correct group according to its key. Groups are created and emitted the first time that an element with a new distinct key value is received from the source sequence.

> [!Note]
> You can manipulate and schedule each of the group sequences downstream using other higher-order operators such as [`Merge`](xref:Bonsai.Reactive.Merge), [`Concat`](xref:Bonsai.Reactive.Concat) or [`Switch`](xref:Bonsai.Reactive.Switch).

The members used to generate the elements in each group sequence can be optionally specified using the <xref href="Bonsai.Reactive.GroupBy.ElementSelector"/> property. If no element selector is specified, the original values from the source sequence will be used.

### Example

Use `GroupBy` to separate out elements from a multiplexed sequence.

:::workflow
![GroupBy Example](../workflows/reactive-groupby-example.bonsai)
:::