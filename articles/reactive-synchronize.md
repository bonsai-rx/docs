---
uid: reactive-synchronize
title: Synchronize
---

![Marble diagram](~/images/reactive-synchronize.svg)

> [!Caution]
> This operator is only used to patch problems in custom implementations of observable sequences that breach the observable contract by emitting notifications concurrently with previous notifications. In almost all situations you should never use this operator.
