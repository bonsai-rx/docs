---
uid: reactive-takewhile
title: TakeWhile
---

![Marble diagram](~/images/reactive-takewhile.svg)

The nested workflow specifying the condition must return a sequence of type <xref href="System.Boolean"/>. This nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence.

After each element is emitted by the source sequence, the latest value from the nested sequence is checked. While the value is `true`, `TakeWhile` will continue to emit all elements from the source sequence. When the value changes to `false`, `TakeWhile` will terminate successfully.
