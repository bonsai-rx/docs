---
uid: reactive-buffercount
title: Buffer
---

![Marble diagram](~/images/reactive-buffercount.svg)

`BufferCount` groups the notifications of the source sequence into chunks containing the number of elements specified in the <xref href="Bonsai.Reactive.BufferCount.Count"/> property. The overlap between the elements in each chunk can be controlled using the <xref href="Bonsai.Reactive.BufferCount.Skip"/> property.

If no skip value is provided, the chunks will be strictly non-overlapping, with a new chunk beginning when the previous chunk ends. If the skip value is less than the specified number of elements, chunks will be overlapping, with a new buffer created every `Skip` notifications. Finally, if the skip value is greater than the specified number of elements, there will be a gap between each chunk where elements from the source sequence will be dropped.
