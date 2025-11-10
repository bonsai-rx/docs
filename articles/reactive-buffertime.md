---
uid: reactive-buffertime
title: BufferTime
---

![Marble diagram](~/images/reactive-buffertime.svg)

The `BufferTime` operator groups the notifications of the source sequence into chunks, where each chunk contains the elements emitted during the specified <xref href="Bonsai.Reactive.BufferTime.TimeSpan"/>. The overlap between the elements in each chunk can be controlled using the <xref href="Bonsai.Reactive.BufferTime.TimeShift"/> property.

If no `TimeShift` is provided, the chunks will be strictly non-overlapping, with a new chunk beginning when the previous chunk ends. If `TimeShift` is smaller than `TimeSpan`, chunks will be overlapping, with a new buffer created every `TimeShift` interval. Finally, if `TimeShift` is larger than `TimeSpan`, there will be a time gap between each chunk where elements from the source sequence may be dropped.

### Example

Use `BufferTime` to group elements into zero or more buffers based on timing information.

:::workflow
![BufferTime Example](../workflows/reactive-buffertime-example.bonsai)
:::

### Related Operators

Use [`BufferCount`](xref:Bonsai.Reactive.BufferCount) instead to group elements into zero or more buffers based on element count.

Use [`WindowTime`](xref:Bonsai.Reactive.WindowTime) instead to create new observable sequences based on timing information.