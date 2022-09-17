---
uid: reactive-take
title: Take
---

![Marble diagram](~/images/reactive-take.svg)

The `Take` operator modifies the source sequence to emit only the specified maximum number of values from the start of the sequence. If the maximum number of values is reached, `Take` will terminate immediately and ignore the remainder of the sequence. `Take` is commonly used to convert an infinite sequence into a finite sequence, for example to take the first key press out of an infinite sequence of keyboard key presses.

`Take` only specifies a maximum upper bound on the number of elements. If the source sequence terminates before that maximum number of values is reached, the behavior of the sequence will not be modified.