---
uid: reactive-timestamp
title: Timestamp
---

![Marble diagram](~/images/reactive-timestamp.svg)

Timestamps are specified relative to Coordinated Universal Time (UTC) using <xref href="System.DateTimeOffset"/> values, and are recorded as soon as element notifications are received from the source sequence.

> [!Warning]
> By default, timestamps are logged using the highest-resolution performance counter available in the system. The clock is synchronized with system time for events ocurring within the same process, including across different threads. However, timestamps are not guaranteed to be synchronized across different processes.

> [!Caution]
> Time recorded using the `Timestamp` operator does not take into account any hardware or communication latency associated with data acquisition processes. If your application requires high-precision timing of data acquisition events, consider logging any available hardware timestamps included in the data, if available.
