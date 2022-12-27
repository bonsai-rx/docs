---
uid: reactive-range
title: Range
---

![Marble diagram](~/images/reactive-range.svg)

The entire sequence of numbers in the range is emitted immediately upon subscription. If another sequence is provided as an input to `Range`, the entire sequence of numbers will be emitted once for each notification in the source sequence.
