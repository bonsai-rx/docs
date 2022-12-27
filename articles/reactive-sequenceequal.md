---
uid: reactive-sequenceequal
title: SequenceEqual
---

![Marble diagram](~/images/reactive-sequenceequal.svg)

`SequenceEqual` will return `false` as soon as one of the sequences emits an element with a different value or in a different order from the other sequences, or if one of the sequences terminates early. If all notifications are equal, `SequenceEqual` will return `true` when all sequences terminate successfully.
