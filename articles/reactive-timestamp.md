---
uid: reactive-timestamp
title: Timestamp
---

![Marble diagram](~/images/reactive-timestamp.svg)

Timestamps are specified relative to Coordinated Universal Time (UTC) using <xref href="System.DateTimeOffset"/> values, and are recorded as soon as element notifications are received from the source sequence.

> [!Warning]
> By default, timestamps are logged using the highest-resolution performance counter available in the system. The clock is synchronized with system time for events occurring within the same process, including across different threads. However, timestamps are not guaranteed to be synchronized across different processes.

> [!Caution]
> Time recorded using the `Timestamp` operator does not take into account any hardware or communication latency associated with data acquisition processes. If your application requires high-precision timing of data acquisition events, consider logging any available hardware timestamps included in the data, if available.

### Example

Use `Timestamp` to timestamp elements that are produced by the source sequence.

:::workflow
![Timestamp Example](../workflows/reactive-timestamp-example.bonsai)
:::

#### Record Data Timestamps

Use `Timestamp` in conjunction with [`CsvWriter`](xref:Bonsai.IO.CsvWriter) to record timestamps for various data streams such as camera frames, sensor readings or key presses.

:::workflow
![Timestamp Application RecordTimestamps](../workflows/reactive-timestamp-application-recordtimestamps.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.System` and `Bonsai.Vision` packages to be installed.