---
uid: reactive-sample
title: Sample
---

![Marble diagram](~/images/reactive-sample.svg)

`Sample` always emits the most recent element received from the source sequence. If multiple elements are received between sampling events, all but the latest element will be dropped from the result sequence. Conversely, elements are never repeated: if no new elements are received between two sampling events, no notifications will be emitted.

> [!Note]
> If the sampler sequence completes successfully, the termination event will be used to sample the latest element from the source sequence, if it exists.
