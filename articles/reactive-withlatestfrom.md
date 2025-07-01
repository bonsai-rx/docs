---
uid: reactive-withlatestfrom
title: WithLatestFrom
---

![Marble diagram](~/images/reactive-withlatestfrom.svg)

The behavior of `WithLatestFrom` is very similar to [`CombineLatest`](xref:Bonsai.Reactive.CombineLatest), but while `CombineLatest` emits a combined value whenever any of the source sequences emits a value, `WithLatestFrom` only emits the combination when the first sequence emits a value (as long as the second sequence has emitted at least one value). 

### Examples

Use `WithLatestFrom` to combine two sources in time.

:::workflow
![WithLatestFrom Example](../workflows/reactive-withlatestfrom-example.bonsai)
:::

#### Video Synchronization

Use [`WithLatestFrom`](xref:Bonsai.Reactive.WithLatestFrom) to combine two sources (e.g. frames from different cameras, or the closest frame to a key press).

:::workflow
![WithLatestFrom Application SynchronizeVideo](../workflows/reactive-withlatestfrom-application-synchronizevideo.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Vision` and `Bonsai.Vision.Design` packages to be installed.

#### Background Subtraction

Use [`WithLatestFrom`](xref:Bonsai.Reactive.WithLatestFrom) to combine a source with a reference value for post-processing (e.g. background subtraction).

:::workflow
![WithLatestFrom Application BackgroundSubtraction](../workflows/reactive-withlatestfrom-application-backgroundsubtraction.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Vision` and `Bonsai.Vision.Design` packages to be installed.

### Alternative

Use [`CombineLatest`](xref:Bonsai.Reactive.CombineLatest) to combine sequences if:
- You have more than two sources
- Need a [higher-order](../articles/higher-order.md) operator
- Need to keep all the values from all the sources