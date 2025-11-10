---
uid: reactive-combinelatest
title: CombineLatest
---

![Marble diagram](~/images/reactive-combinelatest.svg)

`CombineLatest` combines the values from each sequence which are closest in time. Whenever any of the source sequences emits a value (as long as all source sequences have emitted at least one value), `CombineLatest` takes the most recently emitted values from all other sequences and creates the combined result. `CombineLatest` will continue to emit values as long as at least one source sequence remains active (i.e. without terminating).

### Higher-order operator

`CombineLatest` also works as a higher-order operator, so it can take as input a sequence of observable sequences. In this case, it will subscribe to each of the source sequences and start collecting all the latest values from each sequence. As soon as the outer sequence terminates, it will start reactively combining the latest values whenever any sequence changes, just as in the case of using `CombineLatest` with a fixed number of inputs. 

![Higher order](~/images/reactive-combinelatestwindow.svg)

### Examples

Use `CombineLatest` to correlate the closest notifications in time from each source.

:::workflow
![CombineLatest Example](../workflows/reactive-combinelatest-example.bonsai)
:::

> [!Warning]
> As `CombineLatest` emits a combined value whenever *any* of the source sequences emits a new value, the number of values emitted by `CombineLatest` is approximately the sum of the number of values in each sequence. If you want to discard redundant values and use only one of the source sequences as a pacemaker, you can use [`Sample`](xref:Bonsai.Reactive.Sample).

:::workflow
![CombineLatest Example with Sample](../workflows/reactive-combinelatest-example-sample.bonsai)
:::

#### Video Synchronization

Use `CombineLatest` to synchronize video from multiple cameras.

:::workflow
![CombineLatest Application Synchronize Video](../workflows/reactive-combinelatest-application-synchronizevideo.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Dsp`, `Bonsai.Vision` and `Bonsai.Vision.Design` packages to be installed.

### Related Operators

Use [`WithLatestFrom`](xref:Bonsai.Reactive.WithLatestFrom) if you only need to combine two sources and want to discard redundant values.