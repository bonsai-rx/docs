---
uid: reactive-amb
title: Amb
---

![Marble diagram](~/images/reactive-amb.svg)

The `Amb` operator sets up a winner-take-all race condition between all source sequences. The first sequence to emit a notification will gain full control of the output, and all the other sequences will have their subscriptions immediatelly cancelled. `Amb` is most commonly used to ensure only one of many outcomes being evaluated in parallel is propagated.
