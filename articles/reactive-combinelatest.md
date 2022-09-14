---
uid: reactive-combinelatest
title: CombineLatest
---

![Marble diagram](~/images/reactive-combinelatest.svg)

`CombineLatest` combines the values from each sequence which are closest in time. Whenever any of the source sequences emits a value (as long as all source sequences have emitted at least one value), `CombineLatest` takes the most recently emitted values from all other sequences and creates the combined result. `CombineLatest` will continue to emit values as long as at least one source sequence remains active (i.e. without terminating).

`CombineLatest` can be useful to temporally correlate separate sources (e.g. frames from different cameras, or the closest frame to a key press). It can also be useful when combining a sequence containing a single reference value with a possibly infinite sequence of values to be associated with the reference (e.g. subtracting a background from every frame).

> [!Warning]
> Because `CombineLatest` emits a combined value whenever *any* of the source sequences emits a new value, the number of values emitted by `CombineLatest` is approximately the sum of the number of values in each sequence. If you need to discard redundant values you can filter the output, e.g. using [`Sample`](xref:Bonsai.Reactive.Sample) to use one of the source sequences as a master driver.

### Higher-order operator

`CombineLatest` also works as a higher-order operator, so it can take as input a sequence of observable sequences. In this case, it will subscribe to each of the source sequences and start collecting all the latest values from each sequence. As soon as the outer sequence terminates, it will start reactively combining the latest values whenever any sequence changes, just as in the case of using `CombineLatest` with a fixed number of inputs. 

![Higher order](~/images/reactive-combinelatestwindow.svg)
