---
uid: reactive-takeuntil
title: TakeUntil
---

![Marble diagram](~/images/reactive-takeuntil.svg)

`TakeUntil` modifies the source sequence so that values are emitted only until the second sequence produces a value. At that time, `TakeUntil` will terminate immediately and ignore the remainder of the sequence. `TakeUntil` is often used to create a dynamic stop condition for an infinite sequence, e.g. grab frames from a video camera until a key is pressed.

If the source sequence terminates before the second sequence produces a value, `TakeUntil` will also terminate and cancel the subscription to the second sequence.