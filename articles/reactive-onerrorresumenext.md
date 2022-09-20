---
uid: reactive-onerrorresumenext
title: OnErrorResumeNext
---

![Marble diagram](~/images/reactive-onerrorresumenext.svg)

The `OnErrorResumeNext` operator allows you to combine the output of multiple sequences of the same type into a single sequence. `OnErrorResumeNext` subscribes to each sequence in turn, emits all the values from that sequence until termination, and then subscribes to the next sequence, even if the previous sequence has terminated with an error. Each sequence is guaranteed to only start after the previous one terminates.

The resulting sequence will always terminate successfully when the last source sequence has terminated.