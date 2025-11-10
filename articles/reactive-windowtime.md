---
uid: reactive-windowtime
title: WindowTime
---

![Marble diagram](~/images/reactive-windowtime.svg)

The `WindowTime` operator groups the notifications of the source sequence into new observable sequences, where each window contains the elements emitted during the specified <xref href="Bonsai.Reactive.WindowTime.TimeSpan"/>. The overlap between the elements in each window can be controlled using the <xref href="Bonsai.Reactive.WindowTime.TimeShift"/> property.

If no `TimeShift` is provided, the windows will be strictly non-overlapping, with a new window beginning when the previous window ends. If `TimeShift` is smaller than `TimeSpan`, windows will be overlapping, with a new buffer created every `TimeShift` interval. Finally, if `TimeShift` is larger than `TimeSpan`, there will be a time gap between each window where elements from the source sequence may be dropped.

> [!Note]
> You can manipulate and schedule each of the windows downstream using other higher-order operators such as [`Merge`](xref:Bonsai.Reactive.Merge), [`Concat`](xref:Bonsai.Reactive.Concat) or [`Switch`](xref:Bonsai.Reactive.Switch).

### Examples

Use `WindowTime` to group elements into zero or more observable sequences based on timing information.

:::workflow
![WindowTime Example](../workflows/reactive-windowtime-example.bonsai)
:::

### Related Operators

Use [`WindowCount`](xref:Bonsai.Reactive.WindowCount) instead to create new observable sequences based on element count.

Use [`BufferTime`](xref:Bonsai.Reactive.BufferTime) instead to group elements into zero or more buffers based on timing information.