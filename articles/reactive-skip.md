---
uid: reactive-skip
title: Skip
---

![Marble diagram](~/images/reactive-skip.svg)

The `Skip` operator modifies the source sequence to remove the specified number of elements from the start of the sequence. After the maximum number of elements is received, `Skip` will then emit the remaining elements in the sequence. If the source sequence terminates before the specified number of elements is received, `Skip` will terminate without emitting any values.

### Examples

Use `Skip` to remove the specified number of elements from the start of the sequence.

:::workflow
![Skip Example](../workflows/reactive-skip-example.bonsai)
:::

#### Discard Startup Elements 

Use `Skip` to ignore frames from the start of a camera capture sequence (e.g. unstable frames due to auto-exposure adaptation).

:::workflow
![Skip Application SkipVideo](../workflows/reactive-skip-application-skipvideo.bonsai)
:::

### Alternative

Use [`Slice`](xref:Bonsai.Reactive.Slice) to ignore n-th elements from a sequence.