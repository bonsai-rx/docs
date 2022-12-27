---
uid: reactive-skiplast
title: SkipLast
---

![Marble diagram](~/images/reactive-skiplast.svg)

The `SkipLast` operator modifies the source sequence to remove the specified number of elements from the end of the sequence. Because `SkipLast` does not know beforehand which values are the last, it will not emit any notifications until at least the specified number of subsequent elements is received. This means that `SkipLast` has the practical effect of delaying notifications from the source sequence by the specified number of values to skip.

> [!Tip]
> `SkipLast` can often be used when you need to impose a delay in the source sequence using number of elements, rather than a time interval.
