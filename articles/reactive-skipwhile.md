---
uid: reactive-skipwhile
title: SkipWhile
---

![Marble diagram](~/images/reactive-skipwhile.svg)

The nested workflow specifying the condition must return a sequence of type <xref href="System.Boolean"/>. This nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence.

After each element is emitted by the source sequence, the latest value from the nested sequence is checked. While the value is `true`, elements will continue to be dropped from the result sequence. When the value changes to `false`, `SkipWhile` will start emitting all elements from the source sequence.

If the source sequence terminates before the nested workflow returns `false`, `SkipWhile` will terminate without emitting any values.
