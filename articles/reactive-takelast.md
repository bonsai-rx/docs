---
uid: reactive-takelast
title: TakeLast
---

![Marble diagram](~/images/reactive-takelast.svg)

The `TakeLast` operator modifies the source sequence to emit only a specified maximum number of values from the end of the sequence. Since `TakeLast` does not know which elements are the last before the original sequence terminates, it will not emit any value until the completion event is emitted, but will instead keep in memory the specified number of "latest" values. At the time when the source sequence terminates, `TakeLast` will immediately emit all buffered values up to the specified maximum number of elements and then terminate.

Because of this buffering behavior, `TakeLast` will always modify the behavior of the original sequence, regardless of how many values it contains.