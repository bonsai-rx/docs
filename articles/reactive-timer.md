---
uid: reactive-timer
title: Timer
---

![Marble diagram](~/images/reactive-timer.svg)

`Timer` can either generate a single value, if <xref href="Bonsai.Reactive.Timer.Period"/> is not specified, or an infinite sequence of values emitted periodically. The first value of `Timer` is emitted after the specified <xref href="Bonsai.Reactive.Timer.DueTime"/>.

> [!Warning]
> The value of the <xref href="Bonsai.Reactive.Timer.DueTime"/> and <xref href="Bonsai.Reactive.Timer.Period"/> properties cannot be modified after the observable sequence has initialized. If dynamic configuration is necessary, make sure that all properties are immediately configured using property mapping operators.

### Example

Use `Timer` to generate periodic elements.

:::workflow
![Timer Example](../workflows/reactive-timer-example.bonsai)
:::
