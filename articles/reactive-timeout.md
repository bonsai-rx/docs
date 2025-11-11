---
uid: reactive-timeout
title: Timeout
---

![Marble diagram](~/images/reactive-timeout.svg)

Time zero is the start of the sequence (i.e. the moment of subscription). If a new notification arrives before a timeout is reached, the clock is reset.

### Examples

Use `Timeout` to raise an error if the next element is not received within the specified timeout duration.

:::workflow
![Timeout Example](../workflows/reactive-timeout-example.bonsai)
:::