---
uid: reactive-sampleinterval
title: SampleInterval
---

![Marble diagram](~/images/reactive-sampleinterval.svg)

If multiple elements are received during each sampling period, `SampleInterval` will emit only the latest value. However, elements are never repeated: if no new elements are received between two sampling events, no notification will be emitted when the sampling period elapses.
