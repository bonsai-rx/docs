---
uid: reactive-isempty
title: IsEmpty
---

![Marble diagram](~/images/reactive-isempty.svg)

If the source sequence completes before returning any elements, the `IsEmpty` operator will emit a single value `true` before terminating successfully. If the source sequence emits any element, `IsEmpty` will immediately emit a single value `false`, terminate successfully, and cancel the subscription to the source sequence.
