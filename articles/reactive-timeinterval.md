---
uid: reactive-timeinterval
title: TimeInterval
---

![Marble diagram](~/images/reactive-timeinterval.svg)

For each element in the source sequence, `TimeInterval` measures the time elapsed between the arrival of that element and the previous element. Time zero is the start of the sequence (i.e. the moment of subscription).

### Example

Use `TimeInterval` to measure the time elapsed between consecutive elements.

:::workflow
![TimeInterval Example](../workflows/reactive-timeinterval-example.bonsai)
:::

#### Measure Camera Frame Rate

Use `TimeInterval` to calculate the rate of camera frame acquisition.

:::workflow
![TimeInterval Application MeasureFrameRate](../workflows/reactive-timeinterval-application-measureframerate.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Vision` package to be installed.