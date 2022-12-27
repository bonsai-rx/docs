---
uid: reactive-timeout
title: Timeout
---

![Marble diagram](~/images/reactive-timeout.svg)

Time zero is the start of the sequence (i.e. the moment of subscription). If a new notification arrives before a timeout is reached, the clock is reset.
