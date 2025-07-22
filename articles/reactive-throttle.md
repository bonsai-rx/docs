---
uid: reactive-throttle
title: Throttle
---

![Marble diagram](~/images/reactive-throttle.svg)

The `Throttle` operator provides a mechanism to control backpressure in reactive streams. `Throttle` emits an element from the source sequence only if that element is followed by a period of silence longer than <xref href="Bonsai.Reactive.Throttle.DueTime"/>. If new elements are received during this period, the previous element is dropped and the silent period timer is reset.

> [!Warning]
> Any elements emitted by `Throttle` will necessarily be delayed by <xref href="Bonsai.Reactive.Throttle.DueTime"/>, since the only way to test that an element is followed by a period of silence is to wait out the period.

### Example

Use `Throttle` to emit only elements that are followed by a silent period.

:::workflow
![Throttle Example](../workflows/reactive-throttle-example.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.WindowsInput` package to be installed.