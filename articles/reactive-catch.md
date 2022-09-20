---
uid: reactive-catch
title: Catch
---

![Marble diagram](~/images/reactive-catch.svg)

The `Catch` operator allows you to handle error notifications from a sequence by combining the output of multiple fallback sequences of the same type into a single sequence. `Catch` subscribes to the next sequence when the previous sequence produces an error, and emits all the values from that sequence until successful termination. If that sequence also terminates exceptionally, `Catch` then subscribes to the next sequence, and so forth. Each sequence is guaranteed to only start after the previous one terminates.

The resulting sequence will terminate successfully when any of the source sequences has terminated successfully, or exceptionally when all sequences have terminated with an error.