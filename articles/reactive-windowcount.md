---
uid: reactive-windowcount
title: WindowCount
---

![Marble diagram](~/images/reactive-windowcount.svg)

`WindowCount` groups the notifications of the source sequence into new observable sequences containing the number of elements specified in the <xref href="Bonsai.Reactive.WindowCount.Count"/> property. The overlap between the elements in each window can be controlled using the <xref href="Bonsai.Reactive.WindowCount.Skip"/> property.

If no skip value is provided, the windows will be strictly non-overlapping, with a new window beginning when the previous window ends. If the skip value is less than the specified number of elements, windows will be overlapping, with a new window created every `Skip` notifications. Finally, if the skip value is greater than the specified number of elements, there will be a gap between each window where elements from the source sequence will be dropped.

> [!Note]
> You can manipulate and schedule each of the windows downstream using other higher-order operators such as [`Merge`](xref:Bonsai.Reactive.Merge), [`Concat`](xref:Bonsai.Reactive.Concat) or [`Switch`](xref:Bonsai.Reactive.Switch).

### Example

Use `WindowCount` to group elements into zero or more observable sequences based on element count.

:::workflow
![WindowCount Example](../workflows/reactive-windowcount-example.bonsai)
:::

### Related Operators

Use [`WindowTime`](xref:Bonsai.Reactive.WindowTime) instead to create new observable sequences based on timing information.

Use [`BufferCount`](xref:Bonsai.Reactive.BufferCount) instead to group elements into zero or more buffers based on element count.