---
uid: reactive-skip
title: Skip
---

![Marble diagram](~/images/reactive-skip.svg)

The `Skip` operator modifies the source sequence to remove the specified number of values from the start of the sequence. After the maximum number of values is received, `Skip` will then emit the remaining values in the sequence. `Skip` can be used to ignore unstable values from the start of a dynamic time series, e.g. to remove the auto-exposure adaptation start of a camera capture sequence.

If the source sequence terminates before the specified number of values is received, `Skip` will terminate without emitting any values.